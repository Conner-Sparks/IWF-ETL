import pandas as pd
import numpy as np


def get_average_podium_totals(input):
    """
    Returns DataFrame containing the average podium total of each competition
    within database.
    """
    weightclasses = ["45 kg Women", "49 kg Women", "55 kg Women", "59 kg Women", "64 kg Women", 
                     "71 kg Women", "76 kg Women", "81 kg Women", "87 kg Women", "+87 kg Women",
                     "55 kg Men", "61 kg Men", "67 kg Men", "73 kg Men", "81 kg Men", 
                     "89 kg Men", "96 kg Men", "102 kg Men", "109 kg Men", "+109 kg Men"]
    
    comp_ids = input.loc[:, "comp_id"].unique().tolist()
    
    comp_id_column = []
    weightclass_column = []
    podium_average_column = []

    for comp_id in comp_ids:
        
        skip_comp = 0
        
        # df of comp results from a specific competition, indexed by comp_id
        comp_df = input[input['comp_id'] == comp_id].copy()
        
        
        # pre scanning results_dict to ensure all weight classes are represented at 
        # current competition, if they are not, skip to next comp_id
        for class_ in weightclasses:
                        
            class_results = comp_df[comp_df["weightclass"] == class_].copy()
            
            if class_results.empty:
                skip_comp = 1
                break
                
        # skipping current competition
        if skip_comp == 1:
            continue
    
        for class_ in weightclasses:
            
            # df of results from a single weightclass
            class_results = comp_df[comp_df["weightclass"] == class_].copy()
            
            # if class_results.empty:
            #     continue
            
            # calculating "total" column from a specific competition, indexed by comp_id
            for i, row in class_results.iterrows():
                if row["best_sn"] != "---" and row["best_cj"] != "---":
                    total = int(class_results.loc[i, "best_sn"]) + int(class_results.loc[i, "best_cj"])
                    class_results.loc[i, "total"] = total
                    
                # if the athlete failed to post a total, set their total as 0
                else: 
                    class_results.loc[i, "total"] = 0

            class_results.sort_values("total", ascending=False, inplace=True)
        
            # grabbing top 3 athletes and removing those who didn't post a total
            podium_totals = class_results.head(3)["total"]   
            podium_totals = [total for total in podium_totals if total > 0]
            podium_average = np.round(np.mean(podium_totals), 2)
            
            comp_id_column.append(comp_id)
            weightclass_column.append(class_)
            podium_average_column.append(podium_average)
            
    return pd.DataFrame({
                "comp_id" : comp_id_column,
                "weightclass" : weightclass_column,
                "podium_average_total" : podium_average_column
            })
       
    
def get_output_schema():
    return pd.DataFrame({
        "comp_id" : prep_int(),
        "weightclass" : prep_string(),
        "podium_average_total" : prep_decimal()
    })