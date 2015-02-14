#################################################################
# Use test values instead of COM port reading                   #
#################################################################
    ir_buffer = "/LUGC2WR5\r\n"
    ir_lines = ir_buffer.strip().split('\r\n')
    ir_buffer = "6.8(0347.292*GJ)6.26(02647.89*m3)9.21(65298392)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.26*01(02378.83*m3)6.8*01(0311.399*GJ)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "F(0)9.20(65298392)6.35(60*m)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.6(0023.8*kW)6.6*01(0023.8*kW)6.33(000.636*m3ph)9.4(099*C&090*C)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.31(0069294*h)6.32(0000343*h)9.22(R)9.6(000&65298392&0)9.7(20000)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.32*01(0000343*h)6.36(01-01)6.33*01(000.636*m3ph)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.8.1()6.8.2()6.8.3()6.8.4()6.8.5()\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.8.1*01()6.8.2*01()6.8.3*01()\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.8.4*01()6.8.5*01()\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "9.4*01(099*C&090*C)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.36.1(2006-02-17)6.36.1*01(2006-02-17)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.36.2(2011-12-21)6.36.2*01(2011-12-21)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.36.3(2006-03-23)6.36.3*01(2006-03-23)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.36.4(2006-02-21)6.36.4*01(2006-02-21)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "6.36.5(2000-00-00)6.36*02(01)9.36(2013-10-04&12:56:50)9.24(1.5*m3ph)\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "9.17(0)9.18()9.19()9.25()\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "9.1(0&1&0&-&CV&3&2.20)9.2(&&)0.0(65298392)!\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
    ir_buffer = "h0\r\n"
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
