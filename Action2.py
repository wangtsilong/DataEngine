#-------Action2：统计全班的成绩------------
import pandas as pd
score=pd.DataFrame({'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]},
                   index=['张飞','关羽','刘备','典韦','许禇'])
#依次输出每个科目的平均分，最低分，最高分，方差与标准差
for i in score.columns:
    print("{}的平均分为{},最低分为{},最高分为{},方差为{:.3f},标准差为{:.3f}\n".
          format(i,score[i].mean(),score[i].min(),score[i].max(),score[i].var(),score[i].std(),))
#按总分进行排序 
score['总分']=score['语文']+score['数学']+score['英语']
score.sort_values(by=['总分'],inplace=True,ascending=False)
print(score)
