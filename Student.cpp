#include <iostream>
using namespace std;

class bank_acc
{
string cust_name, cust_cont;
int acc_no;
float balance=500, deposit_amt, withdraw_amt;

public: 
void deposit()
  {
 cout<<"\nPlease enter customer name:";
cin>>cust_name;
cout<<"\nPlease enter Account Number:";
cin>>acc_no;
cout<<"\nPlease enter customer contact number:";
cin>>cust_cont;
cout<<"\nEnter the value to be deposited : ";
cin>>deposit_amt;
balance = balance + deposit_amt;

  }

void withdraw()
  {
 cout<<"\nPlease enter customer name:";
cin>>cust_name;
cout<<"\nPlease enter Account Number:";
cin>>acc_no;
cout<<"\nPlease enter customer contact number:";
cin>>cust_cont;
cout<<"\nEnter the value to be withdraw : ";
cin>>withdraw_amt;
if (withdraw_amt<balance) 
{
  balance = balance - withdraw_amt;
}
else
{
    cout<<"\n !!! Your balance is not sufficient !!!\n";
}

  }

   void display()
    {
        cout<<"\nName : "<<cust_name;
        cout<<"\nAccount No : "<<acc_no;
        cout<<"\nCustomer contact no : "<<cust_cont;
        cout<<"\nBalance :"<<balance;
    }
    

};

int main()

{
 bank_acc b1;
    b1.deposit();
    b1.display();

     cout<<"\n\n For Withdrawal ";
     
    b1.withdraw();
    b1.display();

    return 0;
}