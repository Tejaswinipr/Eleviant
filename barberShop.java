// import java.util.Queque;
// import java.util.LinkedList;

class barberShop extends Thread{
public void run(){
    System.out.println("Threaad Running");
}
public static void main(String args[]){
    barberShop b=new barberShop();
    b.start();

    //Queue<String> q=new LinkedList<String>();

}
}

class barber{
char b1,b2;
}

class customers{

}