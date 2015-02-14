################
#Csv output #
################
def csv_heat_telegram():
#New filename every day
    csv_filename=datetime.datetime.strftime(datetime.datetime.today(), "UH50_"+"%Y-%m-%d"+".csv" )
    try:
#If csv_file exists: open it
        csv_file=open(csv_filename, 'rt')
        csv_file.close()
        csv_file=open(csv_filename, 'at', newline='', encoding="utf-8")
        writer = csv.writer(csv_file, dialect='excel', delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    except IOError:
#Otherwise: create it
        csv_file=open(csv_filename, 'wt', newline='', encoding="utf-8")
        writer = csv.writer(csv_file, dialect='excel', delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#Write csv-header
        writer.writerow([
         'heat_timestamp',
         'heat_equipment_id',
         'heat_meterreading_energy',
         'heat_unitmeterreading_energy',
         'heat_meterreading_volume',
         'heat_unitmeterreading_volume',
         'heat_meterreading_hours',
         'heat_unitmeterreading_hours'])
    print ("UH50 telegram in %s gelogd op: %s" % (csv_filename, heat_timestamp) )
    writer.writerow([
         heat_timestamp,
         heat_equipment_id,
         heat_meterreading_energy,
         heat_unitmeterreading_energy,
         heat_meterreading_volume,
         heat_unitmeterreading_volume,
         heat_meterreading_hours,
         heat_unitmeterreading_hours ])
    csv_file.close()

    return
