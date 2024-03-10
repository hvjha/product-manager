from django.db import models

class database(models.Model):
    Date=models.DateTimeField()
    Turbine_Generator=models.IntegerField(max_length=200)
    State_board=models.IntegerField(max_length=200)
    DG=models.IntegerField(max_length=200)
    PSD=models.IntegerField(max_length=200)
    Oral_utility=models.IntegerField(max_length=200)
    FRICK_India=models.IntegerField(max_length=200)
    ORAL_BD_SRP=models.IntegerField(max_length=200)
    LYO=models.IntegerField(max_length=200)
    BD_plant=models.IntegerField(max_length=200)
    Trane_machine=models.IntegerField(max_length=200)
    CSI_02=models.IntegerField(max_length=200)
    Sterile_utility=models.IntegerField(max_length=200)
    STR_A=models.IntegerField(max_length=200)
    LYO_1=models.IntegerField(max_length=200)
    LYO_2=models.IntegerField(max_length=200)
    LYO_3=models.IntegerField(max_length=200)
    STR_C=models.IntegerField(max_length=200)
    AHU_STR_C=models.IntegerField(max_length=200)
    AHU_STR_A=models.IntegerField(max_length=200)
    RO_and_LAB=models.IntegerField(max_length=200)
    LYO_CT_pump_and_sterile_reactor=models.IntegerField(max_length=200)
    Lighting=models.IntegerField(max_length=200)
    Boiler_8_ton=models.IntegerField(max_length=200)
    Fire_hydrand_and_borewell=models.IntegerField(max_length=200)
    Canteen=models.IntegerField()



