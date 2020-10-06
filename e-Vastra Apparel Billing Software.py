from tkinter import *
from tkinter import messagebox
import math,random,os,datetime
class Apparel_Billing:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x950+0+0")
        self.root.title("e-Vastra")

        
        bg_color="#074463"
        title=Label(self.root,text="e-Vastra",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",20,"bold"),pady=2).pack(fill=X)
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=SUNKEN,bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        F1.place(x=0,y=0,relwidth=1)

        #==================customer variables====================

        self.c_name=StringVar()
        self.c_ph=StringVar()
        self.c_landl=StringVar()
        self.billno=StringVar()
        x=random.randint(1,10000)
        self.billno.set(str(x))
        

        #==================Saree variables=======================

        self.ba_q=IntVar()
        self.ba_p=IntVar()
        self.ba_i=StringVar()
        self.i_q=IntVar()
        self.i_p=IntVar()
        self.i_i=StringVar()
        self.ps_q=IntVar()
        self.ps_p=IntVar()
        self.ps_i=StringVar()
        self.dj_q=IntVar()
        self.dj_p=IntVar()
        self.dj_i=StringVar()
        self.c_q=IntVar()
        self.c_p=IntVar()
        self.c_i=StringVar()
        self.t_q=IntVar()
        self.t_p=IntVar()
        self.t_i=StringVar()
        self.k_q=IntVar()
        self.k_p=IntVar()
        self.k_i=StringVar()
        self.balu_q=IntVar()
        self.balu_p=IntVar()
        self.balu_i=StringVar()
        self.s_q=IntVar()
        self.s_p=IntVar()
        self.s_i=StringVar()
        self.j_q=IntVar()
        self.j_p=IntVar()
        self.j_i=StringVar()
        self.r_q=IntVar()
        self.r_p=IntVar()
        self.r_i=StringVar()
        self.fa_q=IntVar()
        self.fa_p=IntVar()
        self.fa_i=StringVar()
        self.cot_q=IntVar()
        self.cot_p=IntVar()
        self.cot_i=StringVar()
        self.ha_q=IntVar()
        self.ha_p=IntVar()
        self.ha_i=StringVar()

        #==================Amount variables=======================

        self.tot_amnt=IntVar()
        self.gst=IntVar()
        self.billamnt=IntVar()
        
        #==================Customer Label=======================
        
        customer_name_label=Label(F1,bg=bg_color,text="Customer Name:",fg="lightblue",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=5)
        customer_name_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        customer_no_label=Label(F1,text="Contact Number:",bg=bg_color,fg="lightblue",font=("times mew roman",15,"bold")).grid(row=0,column=2,padx=10,pady=5)
        customer_no_txt=Entry(F1,width=20,textvariable=self.c_ph,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        customer_no_label=Label(F1,text="Landline Number:",bg=bg_color,fg="lightblue",font=("times mew roman",15,"bold")).grid(row=0,column=4,padx=10,pady=5)
        customer_no_txt=Entry(F1,width=20,textvariable=self.c_landl,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_no_label=Label(F1,text="Bill Number:",bg=bg_color,fg="lightblue",font=("times mew roman",15,"bold")).grid(row=0,column=6,padx=10,pady=5)
        bill_no_txt=Entry(F1,width=15,textvariable=self.billno,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=7,padx=10,pady=5)

        F2=LabelFrame(self.root,text="Product Details",bd=7,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        F2.place(x=10,y=90,width=620,height=700)
        
        #==================Product Details=======================
   
        item_label=Label(F2,text="Items",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=5)
        quantity_label=Label(F2,text="Quantity",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=1,padx=10,pady=5)
        price_label=Label(F2,text="Price",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=10,pady=5)

        ikkat_txt=Entry(F2,textvariable=self.i_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=2,column=0,padx=5,pady=5)
        ikkat_txt_q=Entry(F2,textvariable=self.i_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=2,column=1,padx=5,pady=5)
        ikkat_txt_p=Entry(F2,textvariable=self.i_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=2,column=2,padx=5,pady=5)
        
        puresilk_txt=Entry(F2,textvariable=self.ps_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=3,column=0,padx=5,pady=5)
        puresilk_txt_q=Entry(F2,textvariable=self.ps_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=3,column=1,padx=5,pady=5)
        puresilk_txt_p=Entry(F2,textvariable=self.ps_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=3,column=2,padx=5,pady=5)
        
        dhakaijam_txt=Entry(F2,textvariable=self.dj_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=4,column=0,padx=5,pady=5)
        dhakaijam_txt_q=Entry(F2,textvariable=self.dj_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=4,column=1,padx=5,pady=5)
        dhakaijam_txt_p=Entry(F2,textvariable=self.dj_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=4,column=2,padx=5,pady=5)

        chifon_txt=Entry(F2,textvariable=self.c_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=5,column=0,padx=5,pady=5)
        chifon_txt_q=Entry(F2,textvariable=self.c_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=5,column=1,padx=5,pady=5)
        chifon_txt_p=Entry(F2,textvariable=self.c_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=5,column=2,padx=5,pady=5)
        
        tassar_txt=Entry(F2,textvariable=self.t_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=6,column=0,padx=5,pady=5)
        tassar_txt_q=Entry(F2,textvariable=self.t_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=6,column=1,padx=5,pady=5)
        tassar_txt_p=Entry(F2,textvariable=self.t_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=6,column=2,padx=5,pady=5)
        
        kanjivaram_txt=Entry(F2,textvariable=self.k_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=7,column=0,padx=5,pady=5)
        kanjivaram_txt_q=Entry(F2,textvariable=self.k_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=7,column=1,padx=5,pady=5)
        kanjivaram_txt_p=Entry(F2,textvariable=self.k_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=7,column=2,padx=5,pady=5)
        
        baluchori_txt=Entry(F2,textvariable=self.balu_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=8,column=0,padx=5,pady=5)
        baluchori_txt_q=Entry(F2,textvariable=self.balu_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=8,column=1,padx=5,pady=5)
        baluchori_txt_p=Entry(F2,textvariable=self.balu_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=8,column=2,padx=5,pady=5)
        
        southcotton_txt=Entry(F2,textvariable=self.s_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=9,column=0,padx=5,pady=5)
        southcotton_txt_q=Entry(F2,textvariable=self.s_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=9,column=1,padx=5,pady=5)
        southcotton_txt_p=Entry(F2,textvariable=self.s_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=9,column=2,padx=5,pady=5)

        jardausi_txt=Entry(F2,textvariable=self.j_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=10,column=0,padx=5,pady=5)
        jardausi_txt_q=Entry(F2,textvariable=self.j_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=10,column=1,padx=5,pady=5)
        jardausi_txt_p=Entry(F2,textvariable=self.j_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=10,column=2,padx=5,pady=5)

        rayonsilk_txt=Entry(F2,textvariable=self.r_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=11,column=0,padx=5,pady=5)
        rayonsilk_txt_q=Entry(F2,textvariable=self.r_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=11,column=1,padx=5,pady=5)
        rayonsilk_txt_p=Entry(F2,textvariable=self.r_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=11,column=2,padx=5,pady=5)
    
        fancy_txt=Entry(F2,textvariable=self.fa_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=12,column=0,padx=5,pady=5)
        fancy_txt_q=Entry(F2,textvariable=self.fa_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=12,column=1,padx=5,pady=5)
        fancy_txt_p=Entry(F2,textvariable=self.fa_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=12,column=2,padx=5,pady=5)

        banarasi_txt=Entry(F2,textvariable=self.ba_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=13,column=0,padx=5,pady=5)
        banarasi_txt_q=Entry(F2,textvariable=self.ba_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=13,column=1,padx=5,pady=5)
        banarasi_txt_p=Entry(F2,textvariable=self.ba_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=13,column=2,padx=5,pady=5)


        cottonprint_txt=Entry(F2,textvariable=self.cot_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=14,column=0,padx=5,pady=5)
        cottonprint_txt_q=Entry(F2,textvariable=self.cot_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=14,column=1,padx=5,pady=5)
        cottonprint_txt_p=Entry(F2,textvariable=self.cot_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=14,column=2,padx=5,pady=5)

        
        handloom_txt=Entry(F2,textvariable=self.ha_i,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=15,column=0,padx=5,pady=5)
        handloom_txt_q=Entry(F2,textvariable=self.ha_q,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=15,column=1,padx=5,pady=5)
        handloom_txt_p=Entry(F2,textvariable=self.ha_p,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=15,column=2,padx=5,pady=5)
        
        #==================Amount Details=======================

 
        F3=LabelFrame(self.root,text="Amount Details",bd=7,relief=SUNKEN,font=("times new roman",15,"bold"),bg=bg_color,fg="gold")
        F3.place(x=640,y=100,height=200,width=350)

        totalamount_label=Label(F3,text="Total Amount",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=10,pady=5)
        totalamount_txt=Entry(F3,textvariable=self.tot_amnt,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=0,column=5,padx=5,pady=5)
        gst_label=Label(F3,text="GST",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=4,padx=10,pady=5)
        gst_txt_p=Entry(F3,textvariable=self.gst,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=1,column=5,padx=5,pady=5)
        billamnt_label=Label(F3,text="Billing Amount",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=2,column=4,padx=10,pady=5)
        billamnt_txt_p=Entry(F3,textvariable=self.billamnt,font="arial 10",bd=7,relief=SUNKEN,width=20).grid(row=2,column=5,padx=5,pady=5)

        
        F4=Frame(self.root,bd=7,relief=GROOVE)
        F4.place(x=680,y=320,width=650,height=450)
        
        #==================Billing Area=======================
        
        Label1=Label(F4,text="Billing Area",font="arial 10",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.textarea=Text(F4,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        F5=LabelFrame(self.root,bd=7,relief=GROOVE,bg=bg_color)
        F5.place(x=1000,y=100,height=200,width=385)
        
        #==================Menu Buttons=======================
        
        total_btn=Button(F5,command=self.total,text="Total",bd=10,relief=GROOVE,bg="gray",font=("times new roman",14,"bold")).grid(row=7,column=4,padx=5,pady=5)
        genbill_btn=Button(F5,command=self.genbill,text="Generate Bill",bd=10,relief=GROOVE,bg="gray",font=("times new roman",14,"bold")).grid(row=7,column=5,padx=5,pady=5)
        save_btn=Button(F5,command=self.save_bill,text="Save",bd=10,relief=GROOVE,bg="gray",font=("times new roman",14,"bold")).grid(row=8,column=4,padx=5,pady=5)
        clear_btn=Button(F5,command=self.clear_data,text="Clear",bd=10,relief=GROOVE,bg="gray",font=("times new roman",14,"bold")).grid(row=8,column=5,padx=5,pady=5)
        exit_btn=Button(F5,command=self.Exit_menu,text="Exit",bd=10,relief=GROOVE,bg="gray",font=("times new roman",14,"bold")).grid(row=8,column=6,padx=5,pady=5)
        self.billnote()

        #==================Claculations for Bill Amount =======================
        
    def total(self):
        self.ba_pr=(self.ba_p.get())*(self.ba_q.get())
        self.i_pr=(self.i_p.get())*(self.i_q.get())
        self.ps_pr=(self.ps_p.get())*(self.ps_q.get())
        self.dj_pr=(self.dj_p.get())*(self.dj_q.get())
        self.c_pr=(self.c_p.get())*(self.c_q.get())
        self.t_pr=(self.t_p.get())*(self.t_q.get())
        self.k_pr=(self.k_p.get())*(self.k_q.get())
        self.balu_pr=(self.balu_p.get())*(self.balu_q.get())
        self.s_pr=(self.s_p.get())*(self.s_q.get())
        self.j_pr=(self.j_p.get())*(self.j_q.get())
        self.r_pr=(self.r_p.get())*(self.r_q.get())
        self.fa_pr=(self.fa_p.get())*(self.fa_q.get())
        self.cot_pr=(self.cot_p.get())*(self.cot_q.get())
        self.ha_pr=(self.ha_p.get())*(self.ha_q.get())

        self.tot_sa_amnt=float(
                                self.ba_pr+
                                self.i_pr+
                                self.ps_pr+
                                self.dj_pr+
                                self.c_pr+
                                self.t_pr+
                                self.k_pr+
                                self.balu_pr+
                                self.s_pr+
                                self.j_pr+
                                self.r_pr+
                                self.fa_pr+
                                self.cot_pr+
                                self.ha_pr
                                )
        self.tot_amnt.set(self.tot_sa_amnt)
        if self.tot_sa_amnt>1000:
            self.gst.set(str(self.tot_sa_amnt*0.12))

        else:
            self.gst.set(str(self.tot_sa_amnt*0.05))
        self.billamnt.set(str(self.tot_amnt.get()+self.gst.get()))

    #================== Genarating a Bill=======================
  

    def billnote(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t\t\t\t    Company\t\t\t")
        self.textarea.insert(END,"\n\t\t\t\tCompany Address\t\t")
        self.textarea.insert(END,"\n\t\t\tCompany Phone number:999-9999-9999")
        self.textarea.insert(END,f"\nCustomer name:{self.c_name.get()}")
        self.textarea.insert(END,f"\nContact No:{self.c_ph.get()}")
        self.textarea.insert(END,f"\nBill Number:{self.billno.get()}")
        self.textarea.insert(END,f"\nDate:{datetime.datetime.now()}")
    def genbill(self):
        if self.c_name.get()=="" or self.c_ph.get()=="":
            messagebox.showerror("Attention","Customer details are must")

        if len(self.c_ph.get())!=10:
            
            messagebox.showerror("Attention","invalid mobile number")
        else:
            self.billnote()
            self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            self.textarea.insert(END,"\n\tITEM\t\t\tQUANTITY\t\t\tPRICE")
            self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.ba_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.ba_i.get()}\t\t\t{self.ba_q.get()}\t\t\tRs. {self.ba_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.i_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.i_i.get()}\t\t\t{self.i_q.get()}\t\t\tRs. {self.i_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.ps_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.ps_i.get()}\t\t\t{self.ps_q.get()}\t\t\tRs. {self.ps_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.dj_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.dj_i.get()}\t\t\t{self.dj_q.get()}\t\t\tRs. {self.dj_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.c_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.c_i.get()}\t\t\t{self.c_q.get()}\t\t\tRs. {self.c_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.t_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.t_i.get()}\t\t\t{self.t_q.get()}\t\t\tRs. {self.t_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.k_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.k_i.get()}\t\t\t{self.k_q.get()}\t\t\tRs. {self.k_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.balu_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.balu_i.get()}\t\t\t{self.balu_q.get()}\t\t\tRs. {self.balu_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.s_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.s_i.get()}\t\t\t{self.s_q.get()}\t\t\tRs. {self.s_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.j_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.j_i.get()}\t\t\t{self.j_q.get()}\t\t\tRs. {self.j_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.r_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.r_i.get()}\t\t\t{self.r_q.get()}\t\t\tRs. {self.r_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.fa_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.fa_i.get()}\t\t\t{self.fa_q.get()}\t\t\tRs. {self.fa_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.cot_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.cot_i.get()}\t\t\t{self.cot_q.get()}\t\t\tRs. {self.cot_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            if self.ha_q.get()!=0:
                self.textarea.insert(END,f"\n\t{self.ha_i.get()}\t\t\t{self.ha_q.get()}\t\t\tRs. {self.ha_pr}")
                self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            self.textarea.insert(END,f"\nSub-Total:\t\tRs. {self.tot_amnt.get()}")
            self.textarea.insert(END,f"\nGST Rate: 5% bellow Rs.1000 and 12% above Rs.1000 ")
            self.textarea.insert(END,f"\nTotal Bill Amount(GST included):\t\tRs. {self.billamnt.get()}")
            self.textarea.insert(END,"\n---------------------------------------------------------------------------")
            self.textarea.insert(END,"\n\t\t\t  THANK YOU. VISIT AGAIN\t\t\t\t")
            self.textarea.insert(END,"\n---------------------------------------------------------------------------")

   #==================Save Button Functionality=======================
            
    def save_bill(self):
        opn=messagebox.askyesno("SAVE","Do you want to save the Bill")
        if opn>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("All Bills/"+str(self.billno.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return
    #==================Clear Button Functionality=======================
        
    def clear_data(self):
        clrbtn=messagebox.askyesno("CLEAR","Do you want to clear all data")
        if clrbtn>0:
        #==================Clearing customer variables====================

            self.c_name.set("")
            self.c_ph.set("")
            self.c_landl.set(0)
            self.billno.set("")
            x=random.randint(1,10000)
            self.billno.set(str(x))

        #================== Clearing Saree variables=======================

            self.ba_q.set(0)
            self.ba_p.set(0)
            self.ba_i.set("")
            self.i_q.set(0)
            self.i_p.set(0)
            self.i_i.set("")
            self.ps_q.set(0)
            self.ps_p.set(0)
            self.ps_i.set("")
            self.dj_q.set(0)
            self.dj_p.set(0)
            self.dj_i.set("")
            self.c_q.set(0)
            self.c_p.set(0)
            self.c_i.set("")
            self.t_q.set(0)
            self.t_p.set(0)
            self.t_i.set("")
            self.k_q.set(0)
            self.k_p.set(0)
            self.k_i.set("")
            self.balu_q.set(0)
            self.balu_p.set(0)
            self.balu_i.set("")
            self.s_q.set(0)
            self.s_p.set(0)
            self.s_i.set("")
            self.j_q.set(0)
            self.j_p.set(0)
            self.j_i.set("")
            self.r_q.set(0)
            self.r_p.set(0)
            self.r_i.set("")
            self.fa_q.set(0)
            self.fa_p.set(0)
            self.fa_i.set("")
            self.cot_q.set(0)
            self.cot_p.set(0)
            self.cot_i.set("")
            self.ha_q.set(0)
            self.ha_p.set(0)
            self.ha_i.set("")

        #================== Clearing Amount variables=======================

            self.tot_amnt.set(0)
            self.gst.set(0)
            self.billamnt.set(0)
            
    #==================Exit Button Functionality=======================
            
    def Exit_menu(self):
        exitbtn=messagebox.askyesno("EXIT","Do you want to Exit")
        if exitbtn>0:
            self.root.destroy()
        

root=Tk()
obj=Apparel_Billing(root)
root.mainloop()
