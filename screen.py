# Screen output
def print_heat_telegram():
    print ("---------------------------------------------------------------------------------------")
    print ("Landis & Gyr UH50 telegram ontvangen op: %s" % heat_timestamp)
    print ("Meter fabrikant/type: Landis & Gyr Ultraheat 50")
    print (" 0. 0 - Meter identificatie: %s" % heat_equipment_id )
    print (" 6. 8 - Meterstand Energie: %0.3f %s" % (heat_meterreading_energy, heat_unitmeterreading_energy) )
    print (" 6.26 - Meterstand Volume: %0.3f %s" % (heat_meterreading_volume, heat_unitmeterreading_volume) )
    print (" 6.31 - Meterstand Gebruiksduur: %0.3f %s" % (heat_meterreading_hours, heat_unitmeterreading_hours) )
    print ("Einde UH50 telegram" )
    return