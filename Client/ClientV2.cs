using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System.Net.Sockets;
using Newtonsoft.Json;
using System.Threading;

// 接受信息的格式，分为四个字段：类型、ID、位置、大小
public class FishInfo
{
    public string type;
    public int idx;
    public float[] pos;
    public float scale;
}

// 场景中每条鱼的信息，包括：模型对象，ID，flag，目标点，目标大小
public class FishIns
{
    public GameObject obj;
    public int idx;
    public bool flag; // 用于判断该实例是否得到更新，若没有更新则需要删除掉（将未检测到的鱼移除）。
    public Vector3 target;
    public float scale;
}



public class ClientV2 : MonoBehaviour
{

    static Socket socket;
    int recv_len = 0;
    byte[] readbuff = new byte[1024];

    // 存放接收到信息的地方
    public static Queue<List<FishInfo>> recv_que = new Queue<List<FishInfo>>();

    // 存放场景中所有实例信息的地方：fishins
    public static List<FishIns> fishins = new List<FishIns>();

    // 游戏第一帧时调用
    void Start()
    {
        // 连接Server
        socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        socket.Connect("127.0.0.1", 8888);

        // 开启接收线程，不断接收信息
        Thread recv_t = new Thread(new ThreadStart(recv));
        recv_t.Start();
    }

    // 游戏每一帧调用(主线程)
    void Update()
    {
        // 如果recv_que中有内容（即接受线程收到了信息并存入）
        if (recv_que.Count > 0)
        {
            // 把它取出来（是一个List of FishInfo，即此次检测到的图中所有鱼的信息），命名为fishinfo
            List<FishInfo> fishinfo = recv_que.Dequeue();

            // 遍历fishinfo中每项
            foreach (FishInfo i in fishinfo)
            {
                // 如果该fishinfo项不存在对应的fishins项（即检测到了新鱼的情况），则根据该fishinfo项新建一个FishIns实例，并将其存入fishins
                if (!fishins.Exists(t => t.idx == i.idx))
                {
                    FishIns j = new FishIns();
                    create(j, i);
                    fishins.Add(j);  
                }

                // 如果该fishinfo项存在对应的fishins项（即检测信息已有对应的游戏模型），则根据该fishinfo项更新该fishins项
                else
                {
                    FishIns j = fishins.Find(t => t.idx == i.idx);
                    set(j, i);
                }
            }

            // 待以上更新结束后，找到fishins中所有未更新的项（即此次检测没有该鱼的信息了），场景删除掉这个gameobj以及对应的FishIns实例
            List<FishIns> fishout = fishins.FindAll(t => t.flag == false);
            foreach (FishIns i in fishout)
            {
                Destroy(i.obj); // 删除gameobj
            }
            fishins.RemoveAll(t => t.flag == false); // 删除实例
            

        }
    }

    // 接收线程
    void recv()
    {
        while (true)
        {
            recv_len = socket.Receive(readbuff);
            
            // 如果收到信息
            if (recv_len > 0)
            {
                // 将接收到的byte数组反序列化为List<FishInfo>形式
                string str = Encoding.Default.GetString(readbuff, 0, recv_len);
                List<FishInfo> f = JsonConvert.DeserializeObject<List<FishInfo>>(str);

                // 将该信息放入recv_que队列，以供主线程读取
                recv_que.Enqueue(f);
            }
            Thread.Sleep(100);
        }
    }

    // 根据信息（fishinfo中的一项）来新建一个fishins项
    void create(FishIns fishins, FishInfo fishinfo)
    {
        //ID设置
        fishins.idx = fishinfo.idx;

        //场景中创建对应的gameobject，类型、位置、大小均参照信息设置
        fishins.obj = (GameObject)Instantiate(Resources.Load(fishinfo.type));
        fishins.obj.transform.position = new Vector3(fishinfo.pos[0], fishinfo.pos[1], fishinfo.pos[2]);
        fishins.obj.transform.localScale = new Vector3(fishinfo.scale, fishinfo.scale, fishinfo.scale);

        //给该gameobject挂上move脚本
        fishins.obj.AddComponent<move>().idx= fishinfo.idx;

        //更改标志位为已更新
        fishins.flag = true;
        
        //设置目标位置为信息中位置（实际上不移动）
        fishins.target = new Vector3(fishinfo.pos[0], fishinfo.pos[1], fishinfo.pos[2]);

        //设置目标大小为信息中的大小（实际上不变大小）
        fishins.scale = fishinfo.scale;

    }

    // 根据信息（fishinfo中的一项）来更新一个fishins项
    void set(FishIns fishins, FishInfo fishinfo)
    {
        // 跟上面的create()的后三行同理
        fishins.flag = true;
        fishins.target = new Vector3(fishinfo.pos[0], fishinfo.pos[1], fishinfo.pos[2]);
        fishins.scale = fishinfo.scale;
    }

}

