from django.db import models

class Machine_Usage_Sterile_Utility(models.Model):
    Date=models.DateField()
    Air_Compressor_01=models.IntegerField()
    Air_Compressor_02=models.IntegerField()
    Trane_chilled_water_compressor_01=models.IntegerField()
    Trane_chilled_water_compressor_02=models.IntegerField()
    Chilled_Water_pump_01=models.IntegerField()
    Chilled_Water_pump_02=models.IntegerField()
    Brine_sec_pump_01=models.IntegerField()
    Brine_sec_pump_02=models.IntegerField()
    C_T_Water_Utility_pump_01=models.IntegerField()
    C_T_Water_Utility_pump_02=models.IntegerField()
    C_T_Water_Utility_pump_03=models.IntegerField()
    C_T_W_Fan_Utility_01=models.IntegerField()
    C_T_W_Fan_Utility_02=models.IntegerField()
    CSI_Brine_Machine_01=models.IntegerField()
    CSI_Brine_Machine_02=models.IntegerField()
    CSI_Brine_Primary_Pump_01=models.IntegerField()
    CSI_Brine_Primary_Pump_02=models.IntegerField()
    CSI_Brine_Primary_Pump_03=models.IntegerField()
    LYO_CT_water_pump_01=models.IntegerField()
    LYO_CT_water_pump_02=models.IntegerField()
    LYO_CT_water_pump_03=models.IntegerField()
    LYO_CT_fan=models.IntegerField()
    CSI_Brine_Machine_03=models.IntegerField()

class Machine_usage_Oral_Utility(models.Model):
    Date=models.DateField()
    Brine_Unit_Howden_01=models.IntegerField()
    Brine_Unit_Howden_02=models.IntegerField()
    Chilled_water_howden_unit_01=models.IntegerField()
    Chilled_water_CSI_unit_02=models.IntegerField()
    Air_Compressor_01=models.IntegerField()
    Air_Compressor_02=models.IntegerField()
    Air_Compressor_03=models.IntegerField()
    Brine_PRM_pump_01=models.IntegerField()
    Brine_PRM_pump_02=models.IntegerField()
    Brine_PRM_pump_03=models.IntegerField()
    Brine_SEC_pump_01=models.IntegerField()
    Brine_SEC_pump_02=models.IntegerField()
    Brine_SEC_pump_03=models.IntegerField()
    CHW_PRM_Pump_01=models.IntegerField()
    CHW_PRM_Pump_02=models.IntegerField()
    CHW_PRM_Pump_03=models.IntegerField()
    AWAM_02_feed_pump_01=models.IntegerField()
    AWAM_02_feed_pump_02=models.IntegerField()
    CHW_SEC_pump_03=models.IntegerField()
    CHW_SEC_pump_04=models.IntegerField()
    CHW_SEC_pump_05=models.IntegerField()
    CT_Water_utility_pump_01=models.IntegerField()
    CT_Water_utility_pump_02=models.IntegerField()
    CT_Water_utility_pump_03=models.IntegerField()
    SRP_CT_water_pump_01=models.IntegerField()
    SRP_CT_water_pump_02=models.IntegerField()
    CTW_Fan_utility_01=models.IntegerField()
    SRP_CT_fan_02=models.IntegerField()
    Screw_compressor_low_stage=models.IntegerField()
    Vilter_compressor_High_stage=models.IntegerField()
    MEOH_PRM_pump_01=models.IntegerField()
    MEOH_PRM_pump_02=models.IntegerField()
    MEOH_SEC_pump_01=models.IntegerField()
    MEOH_SEC_pump_02=models.IntegerField()
    MEOH_CT_Water_pump_01=models.IntegerField()
    MEOH_CT_Water_pump_02=models.IntegerField()
    MEOH_CT_fan_01=models.IntegerField()
    MEOH_CT_fan_02=models.IntegerField()
    AVAM_soln_pump_01=models.IntegerField()
    AVAM_soln_pump_02=models.IntegerField()
    CHW_SEC_pump_06=models.IntegerField()
    CT_new_pump_01=models.IntegerField()
    CT_new_pump_02=models.IntegerField()
    CT_new_pump_03=models.IntegerField()
    CT_new_fan_01=models.IntegerField()
    CT_new_fan_02=models.IntegerField()



