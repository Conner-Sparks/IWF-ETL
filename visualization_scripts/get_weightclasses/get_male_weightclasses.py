import pandas as pd

def get_men_results(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    men_results_df = input[input["gender"] == "M"].copy()
    return men_results_df


def get_55kg_men(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    men_results_55kg_df = input[input["bodyweight"] <= 55].copy()
    men_results_55kg_df["weightclass"] = "55 kg Men"
    
    return men_results_55kg_df


def get_61kg_men(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    men_results_61kg_df = input[(input["bodyweight"] > 55) & (input["bodyweight"] <= 61)].copy()
    men_results_61kg_df["weightclass"] = "61 kg Men"
    
    return men_results_61kg_df


def get_67kg_men(input):    
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    men_results_67kg_df = input[(input["bodyweight"] > 61) & (input["bodyweight"] <= 67)].copy()
    men_results_67kg_df["weightclass"] = "67 kg Men"
    
    return men_results_67kg_df


def get_73kg_men(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    men_results_73kg_df = input[(input["bodyweight"] > 67) & (input["bodyweight"] <= 73)].copy()
    men_results_73kg_df["weightclass"] = "73 kg Men"
    
    return men_results_73kg_df


def get_81kg_men(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    men_results_81kg_df = input[(input["bodyweight"] > 73) & (input["bodyweight"] <= 81)].copy()
    men_results_81kg_df["weightclass"] = "81 kg Men"
    
    return men_results_81kg_df


def get_89kg_men(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
     
    men_results_89kg_df = input[(input["bodyweight"] > 81) & (input["bodyweight"] <= 89)].copy()
    men_results_89kg_df["weightclass"] = "89 kg Men"

    return men_results_89kg_df


def get_96kg_men(input):   
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
     
    men_results_96kg_df = input[(input["bodyweight"] > 89) & (input["bodyweight"] <= 96)].copy()
    men_results_96kg_df["weightclass"] = "96 kg Men"

    
    return men_results_96kg_df


def get_102kg_men(input):   
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
     
    men_results_102kg_df = input[(input["bodyweight"] > 96) & (input["bodyweight"] <= 102)].copy()
    men_results_102kg_df["weightclass"] = "102 kg Men"
    
    return men_results_102kg_df


def get_109kg_men(input):   
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
     
    men_results_109kg_df = input[(input["bodyweight"] > 102) & (input["bodyweight"] <= 109)].copy()
    men_results_109kg_df["weightclass"] = "109 kg Men"
    
    return men_results_109kg_df


def get_super_men(input):   
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
        
    men_results_super_df = input[input["bodyweight"] > 109].copy()
    men_results_super_df["weightclass"] = "+109 kg Men"
    
    return men_results_super_df

def get_male_weightclasses(input):
    """_summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
        
    """
    
    men_results = get_men_results(input)
    men_results_55kg = get_55kg_men(men_results)
    men_results_61_kg = get_61kg_men(men_results)
    men_results_67kg = get_67kg_men(men_results)
    men_results_73kg = get_73kg_men(men_results)
    men_results_81kg = get_81kg_men(men_results)
    men_results_89kg = get_89kg_men(men_results)
    men_results_96kg = get_96kg_men(men_results)
    men_results_102kg = get_102kg_men(men_results)
    men_results_109kg = get_109kg_men(men_results)
    men_results_super = get_super_men(men_results)
    
    labeled_men_results_df = pd.concat([men_results_55kg,
                                     men_results_61_kg,
                                     men_results_67kg,
                                     men_results_73kg,
                                     men_results_81kg,
                                     men_results_89kg,
                                     men_results_96kg,
                                     men_results_102kg,
                                     men_results_109kg,
                                     men_results_super],
                                    ignore_index=True)

    return labeled_men_results_df

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