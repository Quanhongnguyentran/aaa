import math
class nguoi:
    def __init__(self , id , name):
        self.id = id
        self.name = name

class Quanly:
    def __init__(self, Sinhvien, Giaovien, Diem, monhoc, Nganh, lop ):
        self.Sinhvien = Sinhvien
        self.Giaovien = Giaovien
        self.Diem = Diem
        self.monhoc = monhoc
        self.Nganh = Nganh
        self.Lop = lop


class Sinhvien(nguoi):
    ql: Quanly

    count = 0

    def __init__(self , id , name ,  diemchuyencan, diemktrgiuaki, diemHocki):
        super().__init__(id,name)
        self.id = id
        self.name = name
        self.diemchuyencan = diemchuyencan
        self.diemktrgiuaki = diemktrgiuaki
        self.diemhocki = diemHocki
        Sinhvien.count += 1

    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def set_diemchuyencan(self, diemchuyencan):
        self.diemchuyencan = diemchuyencan
    def set_diemktrgiuaki(self,diemktrgiuaki):
        self.diemktrgiuaki = diemktrgiuaki
    def set_diemhocki(self,diemHocki):
        self.diemhocki = diemHocki


    def get_diemchuyencan(self):
        return self.diemchuyencan
    def get_diemktrgiuaki(self):
        return  self.diemktrgiuaki
    def get_diemHocki(self):
        return  self.diemhocki


    def show_info(self):
        print(f"\nThông tin Sinh Viên :  \n")
        print(f"Id :  { self.get_id() }")
        print(f"Tên Sinh Viên :  { self.name }")
        print((f"Diemchuyencan: {self.diemchuyencan}"))
        print((f"Diemktrgiuaki: {self.diemktrgiuaki}"))
        print((f"Diemhocki: {self.diemhocki}"))
class Giaovien(nguoi):
    ql: Quanly
    def __init__(self , id , name, monday, nganh, lop):
        super().__init__(id, name)
        self.id = id
        self.name = name
        self.monday = monday
        self.nganh = nganh
        self.lop = lop

    def get_id(self):
        return self.id
    def get_monday(self):
        return self.monday
    def get_nganh(self):
        return self.nganh
    def get_lop(self):
        return self.lop

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def show_infogv(self):
        print(f"\nThông tin Sinh Viên :  \n")
        print(f"Id :  { self.get_id() }")
        print(f"Tên giáo viên :  { self.name }")
        print(f"Môn dạy :  {self.monday}")
        print(f"Ngành :  {self.nganh}")
        print(f"Nhập lớp: {self.lop}")

class Diem:
    ql:Quanly
    def __init__(self , diemchuyencan, diemktrgiuaki, diemHocki,):
        self.diemchuyencan = diemchuyencan
        self.diemktrgiuaki = diemktrgiuaki
        self.diemhocki = diemHocki


    def set_diemchuyencan(self, diemchuyencan):
        self.diemchuyencan = diemchuyencan
    def set_diemktrgiuaki(self,diemktrgiuaki):
        self.diemktrgiuaki = diemktrgiuaki
    def set_diemhocki(self,diemHocki):
        self.diemhocki = diemHocki


    def get_diemchuyencan(self):
        return self.diemchuyencan
    def get_diemktrgiuaki(self):
        return  self.diemktrgiuaki
    def get_diemHocki(self):
        return  self.diemhocki

    def show_infoDiem(self):
        print((f"Diemchuyencan: {self.diemchuyencan}"))
        print((f"Diemktrgiuaki: {self.diemktrgiuaki}"))
        print((f"Diemhocki: {self.diemhocki}"))


class monhoc:
    ql: Quanly
    diem: Diem
    def __init__(self , mon1 , mon2, mon3, mon4 ,monkhac):
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
        self.mon4 = mon4
        self.monkhac = monkhac

    def set_mon1(self,  mon1):
        self.mon1 = mon1
    def set_mon2(self , mon2):
        self.mon2 = mon2
    def set_mon3(self , mon3):
        self.mon3 = mon3
    def set_mon4(self , mon4):
        self.mon4 = mon4
    def set_monkhac(self, monkhac):
        self.monkhac = monkhac

    def get_mon1(self):
        return self.mon1
    def get_mon2(self):
        return  self.mon2
    def get_mon3(self):
        return  self.mon3
    def get_mon4(self):
        return  self.mon4
    def get_monkhac(self):
        return  self.monkhac

    def show_infomh(self):
        print((f"Môn 1: {self.mon1}"))
        print((f"Môn 2: {self.mon2}"))
        print((f"Môn 3: {self.mon2}"))
        print((f"Môn 4: {self.mon2}"))
        print((f"Môn khác: {self.monkhac}"))
class Nganh:
    ql: Quanly
    def __init__(self, tenkhoa,tennganh):
        self.tenkhoa = tenkhoa
        self.tennganh = tennganh

    def set_tenkhoa(self,  tenkhoa):
        self.tenkhoa = tenkhoa
    def set_tennganh(self , tennganh):
        self.tennganh = tennganh

    def get_tenkhoa(self):
        return  self.tenkhoa
    def get_tennganh(self):
        return  self.tennganh

    def show_infonganh(self):
        print((f"Tên Khoa: {self.tenkhoa}"))
        print((f"Tên ngành: {self.tennganh}"))
class Lop:
    ql: Quanly
    def __init__(self, lop1 , lop2, lopkhac):
        self.lop1 = lop1
        self.lop2 = lop2
        self.lopkhac = lopkhac

    def set_lop1(self,  lop1):
        self.lop1 = lop1
    def set_lop2(self , lop2):
        self.lop2 = lop2
    def set_lopkhac(self,lopkhac):
        self.lopkhac = lopkhac

    def get_lop1(self):
        return  self.lop1
    def get_lop2(self):
        return  self.lop2
    def get_lopkhac(self):
        return  self.lopkhac

    def show_infolop(self):
        print((f"Tên lớp 1: {self.lop1}"))
        print((f"Tên lớp 2: {self.lop2}"))
        print((f"Tên lớp khác: {self.lopkhac}"))


