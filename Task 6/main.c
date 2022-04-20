#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <unistd.h>
#include <ifaddrs.h>
#include <netpacket/packet.h>



int main(int argc, char *argv[]){
    struct ifaddrs *interface;
    struct ifaddrs *interfaceIterator = NULL;
    struct sockaddr_ll *socketList;
int sock = socket(AF_INET, SOCK_DGRAM, 0);
if(getifaddrs(&interface)!=-1){
    /*if linkedlist of interfaces is successfully generated, iterate
    over the list and get the HW address for each interface
    since a device could have more than one wireless interface*/
    interfaceIterator = interface;
    while(interfaceIterator!=NULL){
        if(((interfaceIterator->ifa_addr)!=NULL)&&(interfaceIterator->ifa_addr->sa_family== AF_PACKET)){ //if this is an interface address and its socket address family is used for packet tranfer, its probably a wifi interface
            socketList = (struct sockaddr_ll*)interfaceIterator->ifa_addr; //set socketList equal to that interface and use the hardware address attribute of the struct to get the hardware address
            printf("Device MAC ADDRESS for interface: ");
            printf("%s ",interfaceIterator->ifa_name);
            for(int i = 0; i < (socketList->sll_halen);i++){
                //while i is less than the length of the hardware address, print i
                if(i+1< socketList->sll_halen){
                    printf("%02x%s",(socketList->sll_addr[i]),":");
                }
                else{
                    printf("%02x",(socketList->sll_addr[i]));
                }
            }
            printf("\n");
        }
        interfaceIterator = interfaceIterator->ifa_next;
    }
    freeifaddrs(interface);
    //possible free interface iterator
}
else{
    printf("Error with getting interfaces");
}
return 0;
}
