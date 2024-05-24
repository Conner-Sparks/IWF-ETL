import pandas as pd

def get_women_results(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    women_results_df = input[input["gender"] == "F"].copy()
    return women_results_df


def get_45kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_45kg_df = input[input["bodyweight"] <= 45].copy()
    women_results_45kg_df["weightclass"] = "45 kg Women"
    
    return women_results_45kg_df


def get_49kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """

    women_results_49kg_df = input[(input["bodyweight"] > 45) & (input["bodyweight"] <= 49)].copy()
    women_results_49kg_df["weightclass"] = "49 kg Women"

    return women_results_49kg_df

def get_55kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """

    women_results_55kg_df = input[(input["bodyweight"] > 49) & (input["bodyweight"] <= 55)].copy()
    women_results_55kg_df["weightclass"] = "55 kg Women"
    
    return women_results_55kg_df


def get_59kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_59kg_df = input[(input["bodyweight"] > 49) & (input["bodyweight"] <= 59)].copy()
    women_results_59kg_df["weightclass"] = "59 kg Women"
    
    return women_results_59kg_df

def get_64kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_64kg_df = input[(input["bodyweight"] > 59) & (input["bodyweight"] <= 64)].copy()
    women_results_64kg_df["weightclass"] = "64 kg Women"
    
    return women_results_64kg_df


def get_71kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_71kg_df = input[(input["bodyweight"] > 64) & (input["bodyweight"] <= 71)].copy()
    women_results_71kg_df["weightclass"] = "71 kg Women"
    
    return women_results_71kg_df


def get_76kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_76kg_df = input[(input["bodyweight"] > 71) & (input["bodyweight"] <= 76)].copy()
    women_results_76kg_df["weightclass"] = "76 kg Women"
    
    return women_results_76kg_df


def get_81kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_81kg_df = input[(input["bodyweight"] > 76) & (input["bodyweight"] <= 81)].copy()
    women_results_81kg_df["weightclass"] = "81 kg Women"
    
    return women_results_81kg_df


def get_87kg_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_87kg_df = input[(input["bodyweight"] > 81) & (input["bodyweight"] <= 87)].copy()
    women_results_87kg_df["weightclass"] = "87 kg Women"
    
    return women_results_87kg_df


def get_super_women(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    women_results_super_df = input[input["bodyweight"] > 87].copy()
    women_results_super_df["weightclass"] = "+87 kg Women"
    
    return women_results_super_df


def get_female_weightclasses(input):
    """_summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    women_results = get_women_results(input)
    women_results_45kg = get_45kg_women(women_results)
    women_results_49_kg = get_49kg_women(women_results)
    women_results_55kg = get_55kg_women(women_results)
    women_results_59kg = get_59kg_women(women_results)
    women_results_64kg = get_64kg_women(women_results)
    women_results_71kg = get_71kg_women(women_results)
    women_results_76kg = get_76kg_women(women_results)
    women_results_81kg = get_81kg_women(women_results)
    women_results_87kg = get_87kg_women(women_results)
    women_results_super = get_super_women(women_results)
    
    labeled_women_results_df = pd.concat([women_results_45kg,
                                     women_results_49_kg,
                                     women_results_55kg,
                                     women_results_59kg,
                                     women_results_64kg,
                                     women_results_71kg,
                                     women_results_76kg,
                                     women_results_81kg,
                                     women_results_87kg,
                                     women_results_super],
                                    ignore_index=True)

    return labeled_women_results_df

def get_output_schema():
    return pd.DataFrame({
        "comp_id" : prep_int(),
        "name" : prep_string(),
        "gender" : prep_string(),
        "nation" : prep_string(),
        "born" : prep_date(),
        "bodyweight" : prep_decimal(),
        "weightclass" : prep_string(),
        "session" : prep_string(),
        "sn_1" : prep_string(),
        "sn_2" : prep_string(),
        "sn_3" : prep_string(),
        "best_sn" : prep_string(),
        "cj_1" : prep_string(),
        "cj_2" : prep_string(),
        "cj_3" : prep_string(),
        "best_cj" : prep_string()   
    })