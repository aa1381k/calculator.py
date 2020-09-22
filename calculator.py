while 1:

    addad_aval=int(input("enter first number: "))

    alamat=input("alamat ra vared konid: ")

    addad_dovom=int(input("enter second number: "))

    def jam ():

        jam_doo_addad = addad_aval + addad_dovom

        print(jam_doo_addad)

    def manfi ():

        manfi_doo_addad = addad_aval - addad_dovom

        print(manfi_doo_addad)

    def zarb ():

        zarb_doo_addad = addad_aval * addad_dovom

        print(zarb_doo_addad)  

    def tagsim ():

        tagsim_doo_addad = addad_aval / addad_dovom

        print(tagsim_doo_addad)


    if alamat == "+":

        jam()
        
    if alamat == "-":

        manfi()

    if alamat == "*":

        zarb()
        
    if alamat == "/":

        tagsim()
