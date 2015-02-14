################
#DB output     #
################
def db_heat_telegram():
    query = "insert into heat_log values (\'" + \
         heat_timestamp  + "\',\'" + \
         heat_equipment_id + "\',\'" + \
         str(heat_meterreading_energy) + "\',\'" + \
         heat_unitmeterreading_energy + "\',\'" + \
         str(heat_meterreading_volume) + "\',\'" + \
         heat_unitmeterreading_volume + "\',\'" + \
         str(heat_meterreading_hours) + "\',\'" + \
         heat_unitmeterreading_hours + "\')"

#   print(query)

    try:
        db = mysql.connector.connect(user=p1_mysql_user, password=p1_mysql_passwd, host=p1_mysql_host, database=p1_mysql_db)
        c = db.cursor()
        c.execute (query)
        db.commit()
        print ("UH50 telegram in database %s / %s gelogd op: %s" % (p1_mysql_host, p1_mysql_db, heat_timestamp) )
        db.close()
    except:
        show_error()
        print ("Fout bij het openen van / schrijven naar database %s / %s. UH50 Telegram wordt gelogd in csv-bestand."  % (p1_mysql_host, p1_mysql_db))
        csv_heat_telegram()
    return
