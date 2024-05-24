import pandas as pd
import numpy as np

def get_athlete_make_percentages(input):
    """
    Finds athlete's made lift percentage out of all attempts
    """

    athlete_names = input.loc[:, "name"].unique().tolist()
    
    df_names = [] 
    df_num_comps = []
    df_weightclasses = []
    df_nations = []
    
    df_made_sn_percent = []
    df_made_cj_percent = []
    df_made_lift_percent = []
    
    df_made_sn_1_percent = []
    df_made_sn_2_percent = []
    df_made_sn_3_percent = []
    df_made_cj_1_percent = []
    df_made_cj_2_percent = []
    df_made_cj_3_percent = []
    
    df_avg_sn_1 = []
    df_avg_sn_2 = []
    df_avg_sn_3 = []
    df_avg_cj_1 = []
    df_avg_cj_2 = []
    df_avg_cj_3 = []
    
    df_num_sn_attempts = []
    df_num_made_snatches = []
    df_num_missed_snatches = []
    
    df_num_cj_attempts = []
    df_num_made_cjs = []
    df_num_missed_cjs = []
    
    df_num_attempts = []
    df_num_made_attempts = []
    df_num_missed_attempts = []
    
    for athlete in athlete_names:
        
        # grabbing all lifts by a single athlete
        athlete_comps = input[input["name"] == athlete].copy()
        
        snatches = []
        cjs = []
        
        sn_1_column = []
        sn_2_column = []
        sn_3_column = []
        cj_1_column = []
        cj_2_column = []
        cj_3_column = []
        
        for i, row in athlete_comps.iterrows():
            
            snatches.append(row["sn_1"])
            sn_1_column.append(row["sn_1"])
                
            snatches.append(row["sn_2"])      
            sn_2_column.append(row["sn_2"])
            
            snatches.append(row["sn_3"])
            sn_3_column.append(row["sn_3"])
            
            cjs.append(row["cj_1"])
            cj_1_column.append(row["cj_1"])
            
            cjs.append(row["cj_2"])
            cj_2_column.append(row["cj_2"])
            
            cjs.append(row["cj_3"])
            cj_3_column.append(row["cj_3"])
        
        snatches = [i for i in snatches if i != "---"] #[i for i in snatches if "---" not in i and "--" not in i]
        cjs = [i for i in cjs if i != "---"] 
        
        # if athlete has not attempted to post a total in competition, remove
        # them from list and skip
        if len(snatches) == 0 or len(cjs) == 0:
            athlete_names.remove(athlete)
            continue
        
        df_names.append(athlete)
        num_comps = len(athlete_comps)
        df_num_comps.append(num_comps)
        
        num_made_snatches = 0
        num_made_cjs = 0
        
        num_made_sn_1 = 0
        num_made_sn_2 = 0
        num_made_sn_3 = 0
        num_made_cj_1 = 0
        num_made_cj_2 = 0
        num_made_cj_3 = 0
        
        # removing instances where an athlete has passed on an attempt
        sn_1_attempts = [i for i in sn_1_column if i != "---"] #if "---" not in i and "--" not in i
        sn_2_attempts = [i for i in sn_2_column if i != "---"]
        sn_3_attempts = [i for i in sn_3_column if i != "---"]
        cj_1_attempts = [i for i in cj_1_column if i != "---"]
        cj_2_attempts = [i for i in cj_2_column if i != "---"]
        cj_3_attempts = [i for i in cj_3_column if i != "---"]
        
        sn_1 = []
        sn_2 = []
        sn_3 = []
        cj_1 = []
        cj_2 = []
        cj_3 = []
        
        for attempt in snatches:
            if "x" not in attempt:
                num_made_snatches += 1
        
        for attempt in cjs:
            if "x" not in attempt:
                num_made_cjs += 1
        
        for attempt in sn_1_attempts:
            if "x" not in attempt:
                num_made_sn_1 += 1
                sn_1.append(int(attempt))
            elif "x" in attempt:
                sn = int(attempt.split(" ")[0])
                sn_1.append(sn)
                
        for attempt in sn_2_attempts:
            if "x" not in attempt:
                num_made_sn_2 += 1
                sn_2.append(int(attempt))
            elif "x" in attempt:
                sn = int(attempt.split(" ")[0])
                sn_2.append(sn)
                
        
        for attempt in sn_3_attempts:
            if "x" not in attempt:
                num_made_sn_3 += 1
                sn_3.append(int(attempt))
            elif "x" in attempt:
                sn = int(attempt.split(" ")[0])
                sn_3.append(sn)
                
        for attempt in cj_1_attempts:
            if "x" not in attempt:
                num_made_cj_1 += 1
                cj_1.append(int(attempt))
            elif "x" in attempt:
                cj = int(attempt.split(" ")[0])
                cj_1.append(cj)
                
        for attempt in cj_2_attempts:
            if "x" not in attempt:
                num_made_cj_2 += 1
                cj_2.append(int(attempt))
            elif "x" in attempt:
                cj = int(attempt.split(" ")[0])
                cj_2.append(cj)
                
        for attempt in cj_3_attempts:
            if "x" not in attempt:
                num_made_cj_3 += 1
                cj_3.append(int(attempt))
            elif "x" in attempt:
                cj = int(attempt.split(" ")[0])
                cj_3.append(cj)
                
        num_sn_attempts = len(snatches)
        num_missed_snatches = num_sn_attempts - num_made_snatches
        
        df_num_sn_attempts.append(num_sn_attempts)
        df_num_made_snatches.append(num_made_snatches)
        df_num_missed_snatches.append(num_missed_snatches)
        
        num_cj_attempts = len(cjs)
        num_missed_cjs = num_cj_attempts - num_made_cjs
        
        df_num_cj_attempts.append(num_cj_attempts)
        df_num_made_cjs.append(num_made_cjs)
        df_num_missed_cjs.append(num_missed_cjs)
        
        num_attempts = num_sn_attempts + num_cj_attempts
        num_made_attempts = num_made_snatches + num_made_cjs
        num_missed_attempts = num_attempts - num_made_attempts
        
        df_num_attempts.append(num_attempts)
        df_num_made_attempts.append(num_made_attempts)
        df_num_missed_attempts.append(num_missed_attempts)
        
        athlete_made_sn_percent = np.round((num_made_snatches / num_sn_attempts) * 100, 2)
        athlete_made_cj_percent = np.round((num_made_cjs / num_cj_attempts) * 100, 2)
        athlete_made_lift_percent = np.round(((num_made_snatches + num_made_cjs) / (num_sn_attempts + num_cj_attempts)) * 100, 2)
        
        df_made_sn_percent.append(athlete_made_sn_percent)
        df_made_cj_percent.append(athlete_made_cj_percent)
        df_made_lift_percent.append(athlete_made_lift_percent)
        
        if len(sn_1_attempts) != 0:
            sn_1_success_rate = np.round((num_made_sn_1 / len(sn_1_attempts)) * 100, 2)
        else:
            sn_1_success_rate = 0
            
        if len(sn_2_attempts) != 0:
            sn_2_success_rate = np.round((num_made_sn_2 / len(sn_2_attempts)) * 100, 2)
        else:
            sn_2_success_rate = 0
            
        if len(sn_3_attempts) != 0:
            sn_3_success_rate = np.round((num_made_sn_3 / len(sn_3_attempts)) * 100, 2)
        else:
            sn_3_success_rate = 0

        if len(cj_1_attempts) != 0:
            cj_1_success_rate = np.round((num_made_cj_1 / len(cj_1_attempts)) * 100, 2)
        else:
            cj_1_success_rate = 0
            
        if len(cj_2_attempts) != 0:
            cj_2_success_rate = np.round((num_made_cj_2 / len(cj_2_attempts)) * 100, 2)
        else:
            cj_2_success_rate = 0
            
        if len(cj_3_attempts) != 0:
            cj_3_success_rate = np.round((num_made_cj_3 / len(cj_3_attempts)) * 100, 2)
        else:
            cj_3_success_rate = 0
        
        avg_sn_1 = np.round(np.mean(sn_1), 0)
        avg_sn_2 = np.round(np.mean(sn_2), 0)
        avg_sn_3 = np.round(np.mean(sn_3), 0)
        avg_cj_1 = np.round(np.mean(cj_1), 0)
        avg_cj_2 = np.round(np.mean(cj_2), 0)
        avg_cj_3 = np.round(np.mean(cj_3), 0)
        
        df_made_sn_1_percent.append(sn_1_success_rate)
        df_made_sn_2_percent.append(sn_2_success_rate)
        df_made_sn_3_percent.append(sn_3_success_rate)
        df_made_cj_1_percent.append(cj_1_success_rate)
        df_made_cj_2_percent.append(cj_2_success_rate)
        df_made_cj_3_percent.append(cj_3_success_rate)
        
        df_avg_sn_1.append(avg_sn_1)
        df_avg_sn_2.append(avg_sn_2)
        df_avg_sn_3.append(avg_sn_3)
        df_avg_cj_1.append(avg_cj_1)
        df_avg_cj_2.append(avg_cj_2)
        df_avg_cj_3.append(avg_cj_3)
        
        # Handling instances where an athlete has competed in multiple weightclasses internationally
        athlete_weightclass = athlete_comps["weightclass"].unique().tolist()
        if len(athlete_weightclass) > 1:
            unique_weightclasses = ""
            for i, string in enumerate(athlete_weightclass):
                class_ = string.split(" ")[0]
                unique_weightclasses += class_
                if i < (len(athlete_weightclass) - 1):
                    unique_weightclasses += "/"
                elif i == (len(athlete_weightclass) - 1):
                    unique_weightclasses += " " + string.split(" ")[1]
                    unique_weightclasses += " " + string.split(" ")[2]
            df_weightclasses.append(unique_weightclasses)
        else:
            df_weightclasses.append(athlete_weightclass[0])
        
        # Handling instances where an athlete has competed for multiple nations internationally
        athlete_nation = athlete_comps["nation"].unique().tolist()
        if len(athlete_nation) > 1:
            unique_nations = ""
            for i, nation in enumerate(athlete_nation):
                unique_nations += nation 
                if i < (len(athlete_nation) - 1):
                    unique_nations += "/"
            df_nations.append(unique_nations)
        else:
            df_nations.append(athlete_nation[0])
            
    return pd.DataFrame({
        "Name" : df_names,
        "Nation" : df_nations,
        "Weightclass" : df_weightclasses,
        "Num Comps" : df_num_comps,
        "% Snatches Successful" : df_made_sn_percent,
        "% SN 1st Attempts Successful" : df_made_sn_1_percent,
        "% SN 2nd Attempts Successful" : df_made_sn_2_percent,
        "% SN 3rd Attempts Successful" : df_made_sn_3_percent,
        "Avg. SN 1st Attempt" : df_avg_sn_1,
        "Avg. SN 2nd Attempt" : df_avg_sn_2,
        "Avg. SN 3rd Attempt" : df_avg_sn_3,
        "% Clean & Jerks Successful" : df_made_cj_percent,
        "% CJ 1st Attempts Successful" : df_made_cj_1_percent,
        "% CJ 2nd Attempts Successful" : df_made_cj_2_percent,
        "% CJ 3rd Attempts Successful" : df_made_cj_3_percent,
        "Avg. CJ 1st Attempt" : df_avg_cj_1,
        "Avg. CJ 2nd Attempt" : df_avg_cj_2,
        "Avg. CJ 3rd Attempt" : df_avg_cj_3,
        "% Attempts Successful" : df_made_lift_percent,
        "Num Snatch Attempts" : df_num_sn_attempts,
        "Num Made Snatches" : df_num_made_snatches,
        "Num Missed Snatches" : df_num_missed_snatches,
        "Num CJ Attempts" : df_num_cj_attempts,
        "Num Made CJs" : df_num_made_cjs,
        "Num Missed CJs" : df_num_missed_cjs,
        "Num Total Attempts" : df_num_attempts,
        "Num Total Made Attempts" : df_num_made_attempts,
        "Num Total Missed Attempts" : df_num_missed_attempts
    })

def get_output_schema():
    return pd.DataFrame({
        "Name" : prep_string(),
        "Nation" : prep_string(),
        "Weightclass" : prep_string(),
        "Num Comps" : prep_int(),
        "% Snatches Successful" : prep_decimal(),
        "% SN 1st Attempts Successful" : prep_decimal(),
        "% SN 2nd Attempts Successful" : prep_decimal(),
        "% SN 3rd Attempts Successful" : prep_decimal(),
        "Avg. SN 1st Attempt" : prep_int(),
        "Avg. SN 2nd Attempt" : prep_int(),
        "Avg. SN 3rd Attempt" : prep_int(),
        "% Clean & Jerks Successful" : prep_decimal(),
        "% CJ 1st Attempts Successful" : prep_decimal(),
        "% CJ 2nd Attempts Successful" : prep_decimal(),
        "% CJ 3rd Attempts Successful" : prep_decimal(),
        "Avg. CJ 1st Attempt" : prep_int(),
        "Avg. CJ 2nd Attempt" : prep_int(),
        "Avg. CJ 3rd Attempt" : prep_int(),
        "% Attempts Successful" : prep_decimal(),
        "Num Snatch Attempts" : prep_int(),
        "Num Made Snatches" : prep_int(),
        "Num Missed Snatches" : prep_int(),
        "Num CJ Attempts" : prep_int(),
        "Num Made CJs" : prep_int(),
        "Num Missed CJs" : prep_int(),
        "Num Total Attempts" : prep_int(),
        "Num Total Made Attempts" : prep_int(),
        "Num Total Missed Attempts" : prep_int()
    })