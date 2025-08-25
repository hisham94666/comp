#include<studio.h>
#include<conio.h>
void main()
{
    int m1,m2,m3,m4,m5,total;
    clrscr();
    printf("enter the marks in 5 subjects");
    scanf("%d%d%d%d%d",&m1,&m2,&m3,&m4,&m5);
    total=m1+m2+m3+m4+m5+
    avg=total/5.O;
    printf("\n marks in subject 1=%d",m1);
    printf("\n marks in subject 2=%d",m2);
    printf("\n marks in subject 3=%d",m3);
    printf("\n marks in subject 4=%d",m4);
    printf("\n marks in subject 5=%d",m5);
      printf("\n Total marks is %d", total);
 printf("\n Average marks is %.2f", avg);
 if(m1<35||m2<35||m3<35||m4<35||m5<35)
 {
  printf("\n Result=Fail");
 }
 else if(avg>=85)
 {
  printf("\n Result=Distinction");
 }
 else if(avg>=70)
 {
  printf("\n Result=First class");
 }
 else if(avg>=55)
 {
  printf("\n Result=Second class");
 }
 else 
 {
  printf("\n Result=Pass");
 }
 getch();
 
}