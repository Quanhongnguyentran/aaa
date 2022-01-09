from student import Sinhvien
from student import Giaovien
from student import monhoc
from student import Nganh
from student import Lop

ds = []
dsgv = []
dsmh = []
dsnganh = []
dsl = []
while True:
    print(f'''\n
        0. Thoát Chương trình
        1. Sinh Viên
            11 Thêm Sinh Viên
            12 Cập nhật thông tin sinh viên
            13 Xóa sinh viên
            14 Xem thông tin tất cả sinh viên
            15 Xem Thông tin sinh viên
            16 Tìm sinh viên theo Tên
            17 Số lượng Sinh viên
        2 Giáo Viên
            21 Thêm Giáo Viên
            22 Cập nhật thông tin giáo viên
            23 Xóa giáo viên
            24 Xem thông tin tất cả giáo viên
            25 Xem Thông tin giáo viên
            26 Tìm giáo viên theo Tên
            27 Số lượng giáo viên
        3 Môn Học
            31 Thêm môn học
            32 Xóa môn học
            33 Xem tất cả môn học
            34 Tìm môn học
            35 Số lượng môn học
        4 Điểm
            41 Xem thông tin tất cả điểm sinh viên
            42 Xem Thông tin điểm sinh viên
        5 Ngành
            51 Thêm ngành
            52 Xóa ngành
            53 Xem tất cả ngành
            54 Tìm ngành
            55 Số lượng ngành
        6 Lớp
            61 Thêm lớp
            62 xóa lớp
            63 Xem tất cả lớp
            64 Tìm lớp
            65 Số lượng lớp

        ''')
    select = input("Mời chọn chức năng:  ")
    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 11:
            id = input("Nhập Id Sinh viên:  ")
            name = input("Nhập Tên Sinh viên:  ")
            diemchuyencan = input("Nhập Điểm chuyên cần: ")
            diemktrgiuaki = input("Nhập điểm ktr giữa kì: ")
            diemhocki = input("Nhập điểm học kì: ")
            sv = Sinhvien(id, name, diemchuyencan, diemktrgiuaki, diemhocki )
            ds.append(sv)
        elif select == 12:
            id = input("Nhập Id sinh Viên bạn cần sửa :  ")
            for i in ds:
                if i.get_id() == id:
                    i.set_Name(input("Nhập vào tên mới:  "))
                    i.show_info()
        elif select == 14:
            if len(ds) == 0:
                print("\n hiện không có sinh viên . Bạn vui lòng thêm sinh viên mói vào danh sách !")
            else:
                print(f"\nHiện có {len(ds)} Sinh viên ")
                for i in ds:
                    i.show_info()
        elif select == 13:
            id = input("Nhập Id Sinh viên cần xóa :  ")
            for i in ds:
                if i.get_id() == id:
                    ds.remove(i)
                    print("Bạn đã xóa sinh viên thành công ")
                    continue
        elif select == 15:
            id = input("Nhập Id Sinh Viên cần xem thông tin :  ")
            for i in ds:
                if i.get_id() == id:
                    i.show_info()
                    continue
        elif select == 16:
            ten = input("Nhập Tên Sinh Viên cần tìm :  ")
            for i in ds:
                if i.get_Name() == ten:
                    i.show_info()
        elif select == 17:
            print(f"\nHiện có {len(ds)} Sinh Viên \n")
        elif select == 21:
            idgv = input("Nhập Id Giáo viên:  ")
            name = input("Nhập Tên Giáo viên:  ")
            monday = input("Nhập môn dạy: ")
            nganh = input("Nhập ngành: ")
            lop = input("Nhập lớp: ")
            gv = Giaovien(idgv, name, monday, nganh, lop)
            dsgv.append(gv)
        elif select == 22:
            idgv = input("Nhập Id Giáo Viên bạn cần sửa :  ")
            for i in dsgv:
                if i.get_id() == idgv:
                    i.set_Name(input("Nhập vào tên mới:  "))
                    i.show_infogv()
        elif select == 24:
            if len(dsgv) == 0:
                print("\n hiện không có Giáo viên . Bạn vui lòng thêm Giáo viên mới vào danh sách !")
            else:
                print(f"\nHiện có {len(dsgv)} Giáo viên ")
                for i in dsgv:
                    i.show_infogv()
        elif select == 23:
            idgv = input("Nhập Id Giáo viên cần xóa :  ")
            for i in dsgv:
                if i.get_id() == idgv:
                    dsgv.remove(i)
                    print("Bạn đã xóa giáo viên thành công ")
                    continue
        elif select == 25:
            idgv = input("Nhập Id Giáo Viên cần xem thông tin :  ")
            for i in dsgv:
                if i.get_id() == idgv:
                    i.show_infogv()
                    continue
        elif select == 26:
            ten = input("Nhập Tên Giáo Viên cần tìm :  ")
            for i in dsgv:
                if i.get_Name() == ten:
                    i.show_infogv()
        elif select == 17:
            print(f"\nHiện có {len(dsgv)} Giáo \n")
        elif select == 31:
            mon1 = input("Nhập môn 1:  ")
            mon2 = input("Nhập môn 2:  ")
            mon3 = input("Nhập môn 3:  ")
            mon4 = input("Nhập môn 4:  ")
            monkhac = input("Nhập môn khác: ")
            mh = monhoc(mon1, mon2, mon3, mon4, monkhac)
            dsmh.append(mh)
        elif select == 33:
            if len(dsmh) == 0:
                print("\n hiện không có môn hoc . Bạn vui lòng thêm môn học mới vào danh sách !")
            else:
                print(f"\nHiện có những môn học ")
                for i in dsmh:
                    i.show_infomh()
        elif select == 32:
            mon = input("Nhập môn cần xóa :  ")
            for i in dsmh:
                if i.get_mon1() == mon:
                    dsmh.remove(i)
                    print("Bạn đã xóa môn học thành công ")
                    continue
        elif select == 34:
            mon = input("Nhập môn học cần tìm :  ")
            for i in dsmh:
                if i.get_mon1() == mon:
                    i.show_infomh()
        elif select == 35:
            print(f"\nHiện có {len(dsmh)} môn học \n")
        elif select == 41:
            if len(ds) == 0:
                print("\n hiện không có điểm sinh viên . Bạn vui lòng thêm điểm mới sinh viên vào danh sách !")
            else:
                print(f"\nHiện có {len(ds)} Sinh viên có điểm ")
                for i in ds:
                    i.show_info()
        elif select == 42:
            id = input("Nhập Sinh Viên cần xem điểm :  ")
            for i in ds:
                if i.get_id() == id:
                    i.show_info()
                    continue
        elif select == 51:
            tenkhoa = input("Nhập tên Khoa:  ")
            tennganh = input("Nhập Tên Ngành:  ")
            nganh = Nganh(tenkhoa, tennganh, )
            dsnganh.append(nganh)
        elif select == 53:
            if len(dsnganh) == 0:
                print("\n hiện không có ngành . Bạn vui lòng thêm ngành mới vào danh sách !")
            else:
                print(f"\nHiện có {len(dsnganh)} ngành ")
                for i in dsnganh:
                    i.show_infonganh()
        elif select == 52:
            tennganh = input("Nhập ngành cần xóa :  ")
            for i in dsnganh:
                if i.get_tennganh() == tennganh:
                    dsnganh.remove(i)
                    print("Bạn đã xóa ngành thành công ")
                    continue
        elif select == 54:
            ten = input("Nhập Tên ngành cần tìm :  ")
            for i in dsnganh:
                if i.get_tennganh() == ten:
                    i.show_infonganh()
        elif select == 55:
            print(f"\nHiện có {len(dsnganh)} ngành \n")

        elif select == 61:
            lop1 = input("Nhập lớp 1:  ")
            lop2 = input("Nhập lớp 2:  ")
            lopkhac = input("Nhập lớp khác:  ")
            lop = Lop(lop1, lop2, lopkhac)
            dsl.append(lop)

        elif select == 63:
            if len(dsl) == 0:
                print("\n hiện không có lớp . Bạn vui lòng thêm lớp mới vào danh sách !")
            else:
                print(f"\nHiện có {len(dsl)} lớp ")
                for i in dsl:
                    i.show_infolop()
        elif select == 62:
            lop1 = input("Nhập lớp cần xóa :  ")
            for i in dsl:
                if i.get_lop1() == lop1:
                    dsl.remove(i)
                    print("Bạn đã xóa lớp thành công ")
                    continue
        elif select == 64:
            ten = input("Nhập Tên ngành cần tìm :  ")
            for i in dsl:
                if i.get_lop1() == ten:
                    i.show_infolop()
        elif select == 65:
            print(f"\nHiện có {len(dsl)} ngành \n")

    else:
        print("\nBạn phải nhập số. Vui Lòng nhập lại !")



