from datetime import date
import pandas as pd

def checkDateFormat(now_year, obj):
    """检查输入，返回完整日期"""
    schedule_date = obj.split("-")
    if len(schedule_date) == 3 and isinstance(schedule_date, list):
        return obj
    elif len(schedule_date) == 2 and isinstance(schedule_date, list):
        return now_year + '-' + obj
    else:
        print("FormatError!Try again.")
        obj = input("Check my schedule for:").strip()
        return checkDateFormat(now_year, obj)

def im_tasks_add(identity):
    """增添ImportantTasks.csv"""
    importantTasks = importantTasks[importantTasks['Identity' != identity]]
    importantTasks.to_csv('reminderData/ImportantTasks.csv')

def im_tasks_del(row):
    """删减ImportantTasks.csv"""
    importantTasks[len(importantTasks)] = row
    importantTasks.to_csv('reminderData/ImportantTasks.csv')

# 初始信息
nowDate = str(date.today())
nowYear = nowDate.split("-")[0]
importantTasks = pd.read_csv('reminderData/ImportantTasks.csv')

while True:
    # 程序运行
    print("-" * 40)
    print("-" * 40)
    
    print(f"Today:{nowDate}")
    print("-" * 40)

    # 提示重要事项
    print("Important Tasks:")
    print("*" * 40)
    print(importantTasks.to_string(index=False))
    print("*" * 40)

    # 规范化文件名，文件路径
    temp = input("Check my schedule for:").strip()
    if temp == 'q' or temp == 'Q':
        input("----------EXIT----------")
        break
    scheduleDate = checkDateFormat(nowYear, temp)
    filePath = "reminderData/" + scheduleDate + ".csv"

    # 检验文件存在，读取文件至df
    try:
        df = pd.read_csv(filePath)
    except FileNotFoundError:
        df = pd.DataFrame()

    while True:
        # 打印已有项
        print("\n\n")
        print('-' * 40)
        print(f"{scheduleDate}:\n")
        print(df)
            
        # 修改程序循环
        ui = input(">>>")
            
        if ui == 'a' or ui == 'A':
            # 增添新项
            addition = input("add>>>")
            # 计算标识符
            new_identity = scheduleDate + '-' + str(len(df))
            # 更改标识符
            new_row = {'Date': scheduleDate, 
                   'State': '_', 
                   'Task': addition, 
                   'Identity': new_identity}
            df.loc[len(df)] = new_row
            # 储存
            df.to_csv(filePath)
                
        elif ui == 'f' or ui == 'F':
            # 完成项
            try:
                finish = int(input("finish>>>"))
                state_past = df[finish, 1]
            except:
                print("----------Error----------")
            # 更新状态
            if state_past == '*':
                im_tasks_del(df[finish, -1])
                df.iloc[finish, 1] = '√'
            else:
                df.iloc[finish, 1] = '√'
            # 储存
            df.to_csv(filePath)
            
        elif ui == 'p' or ui == 'P':
            # 优先项
            try:
                priority = input("prioritize>>>")
                state_past = df[finish, 1]
            except:
                print("----------Error----------")
            # 更新状态
            df.iloc[priority, 1] = '*'
            # 更新ImportantTasks.csv
            im_tasks_add(df.loc[priority])
            # 储存
            df.to_csv(filePath)
            
        else:
            # 储存
            df.to_csv(filePath)
            input("----------Break----------")
            break