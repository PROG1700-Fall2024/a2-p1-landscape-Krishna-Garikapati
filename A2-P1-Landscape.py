#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:   W0502117  
#Student Name:  Krishna Priyanka Garikapati


def main():
        
    #Input values
    Housenumber=int(input("Enter House Number: "))
    depth=float(input("Enter property depth (feet): "))
    width=float(input("Enter property width (feet): "))
    GrassType=input("Enter type of grass (fescue, bentgrass, campus): ")
    Trees=int(input("Enter the number of trees: "))

    # Calculation
    surfaceArea=depth*width
    TreeCharge=Trees*100
    Baselabourcharge=1000
    #Area<=5000 sq ft
    if surfaceArea<=5000:
                if GrassType.lower()=="fescue":
                    GrassPrice=0.05*surfaceArea
                elif GrassType.lower()=="bentgrass":
                    GrassPrice=0.02*surfaceArea
                elif GrassType.lower()=="campus":
                    GrassPrice=0.01*surfaceArea
                else:
                    print("error,Please re-enter correct grass type")
                TotalCost=Baselabourcharge+GrassPrice+TreeCharge
    #Area>5000 sq ft
    elif surfaceArea>5000:
                if GrassType.lower()=="fescue":
                    GrassPrice=0.05*surfaceArea
                elif GrassType.lower()=="bentgrass":
                    GrassPrice=0.02*surfaceArea
                elif GrassType.lower()=="campus":
                    GrassPrice=0.01*surfaceArea
                else:
                    print("error,Please re-enter correct grass type")
                TotalCost=Baselabourcharge+GrassPrice+TreeCharge+500
    print("Total cost for house ",Housenumber, "is: ${0:.2f}".format(TotalCost))
main()
