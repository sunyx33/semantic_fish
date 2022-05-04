using System.Collections;
using System.Collections.Generic;
using UnityEngine;



public class move : MonoBehaviour
{

    public Vector3 start;       // 起始点
    public Vector3 end;         // 终点
    public Vector3 path;        // 路径（转向用）
    public Vector3 scale_sta;   // 起始大小
    public Vector3 scale_end;   // 终止大小
    public float distance;      // 距离（起点与终点间）（为保证定时到达，需要计算速度）
    public float scale_dis;     // 距离（起始大小与终止大小间）（为保证定时到达，需要计算速度）
    public float during = 0.5f; // 定时到达的时间（应与检测间隔对应）
    public int idx;             // 该gameobj所属的FishIns的ID
    float scale;                // 终止大小（float版）


    public void Start()
    {
        start = this.transform.position;
        scale_sta = this.transform.localScale;
    }


    public void Update()
    {
        // 根据ID去找该gameobj对应的目标点与目标大小
        end = ClientV2.fishins.Find(t => t.idx == this.idx).target;
        scale = ClientV2.fishins.Find(t => t.idx == this.idx).scale;
        scale_end = new Vector3(scale, scale, scale);

        // 没游到位置
        if (this.transform.position != end)
        {
            distance = Vector3.Distance(start, end);
            path = end - start;
            // 那就游
            move2(end, during);
        }
        // 游到了
        else
        {
            // 将当前位置作为新起点
            start = this.transform.position;
            // 更改该gameobj对应的FishIns为未更新状态
            ClientV2.fishins.Find(t => t.idx == this.idx).flag = false;
        }

        // 没变到指定大小
        if(this.transform.localScale != scale_end)
        {
            scale_dis = Vector3.Distance(scale_sta, scale_end);
            // 那就变
            this.transform.localScale = Vector3.MoveTowards(transform.localScale, scale_end, (scale_dis / during) * Time.deltaTime);
        }
        // 变到了
        else
        {
            // 将当前大小作为新起点大小
            scale_sta = this.transform.localScale;
        }

    }

    public void move2(Vector3 target, float during)
    {
        // 平移
        this.transform.position = Vector3.MoveTowards(transform.position, target, (distance / during) * Time.deltaTime);

        // 转向
        if (path[0] > 0)
        {
            this.transform.rotation = Quaternion.Euler(new Vector3(180, 90, 0));
        }
        else
        {
            this.transform.rotation = Quaternion.Euler(new Vector3(180, -90, 0));
        }

    }


}