%Cargar las Matrices de Potencia
fid=fopen('MP/Pelamis.txt');
Puntos=[];
pelamis=[];
for i=2:17
    aux= str2num(fgetl(fid));
    pelamis=[pelamis; aux];
end
fclose(fid);
fid=fopen('MP/Ceto.txt');
ceto=[];
for i=2:15
    aux=str2num(fgetl(fid));
    ceto=[ceto; aux];
end
fclose(fid);
fid=fopen('MP/Energy buoy.txt');
energy_buoy=[];
for i=2:15
    aux=str2num(fgetl(fid));
    energy_buoy=[energy_buoy; aux];
end
fclose(fid);
fid=fopen('MP/Oceantec.txt');
oceantec=[];
for i=2:11
    aux=str2num(fgetl(fid));
    oceantec=[oceantec; aux];
end
fclose(fid);
fid=fopen('MP/Oyster Energy.txt');
oyster_energy=[];
for i=2:15
    aux=str2num(fgetl(fid));
    oyster_energy=[oyster_energy; aux];
end
fclose(fid);
fid=fopen('MP/PPC.txt');
ppc=[];
for i=2:15
    aux=str2num(fgetl(fid));
    ppc=[ppc; aux];
end
fclose(fid);
fid=fopen('MP/Seabed.txt');
seabed=[];
for i=2:15
    aux=str2num(fgetl(fid));
    seabed=[seabed; aux];
end
fclose(fid);
fid=fopen('MP/seapower.txt');
seapower=[];
for i=2:17
    aux=str2num(fgetl(fid));
    seapower=[seapower; aux];
end
fclose(fid);
fid=fopen('MP/Wavestar.txt');
wavestar=[];
for i=2:11
    aux=str2num(fgetl(fid));
    wavestar=[wavestar; aux];
end
fclose(fid);
PM={pelamis,seapower,wavestar,oceantec,ppc,energy_buoy,ceto,seabed,oyster_energy};
maximo=zeros(1,9);
for i=1:9
    aux=max(max(PM{i})); %obtenemos la potencia m�xima que puede generar cada aparato
    maximo(1,i)=aux;
end
clear aux
limites=[];
for i=1:9
    aux=PM{i};
    c_ini=aux(1,2);
    c_fin=aux(1,end);
    f_ini=aux(2,1);
    f_fin=aux(end,1);
    limites=[limites;c_ini,c_fin,f_ini,f_fin];
end
% aqu� empiezo a cargar los datos de los puntos SIMAR
documentos=dir('D:\Dani\Puertos\txt');
documentos(1:2)=[];
for k=1:length(documentos)
    fid=fopen(strcat('D:\Dani\Puertos\txt\',documentos(k).name)','r');
    fgetl(fid);
    fid=fopen(strcat('D:\Dani\Puertos\txt\',documentos(k).name)','r');
    fgetl(fid);
    fgetl(fid);
    fgetl(fid);
    M=[];
    fgets(fid,16);
    id=str2num(fgets(fid,7));
    fgetl(fid);
    fgets(fid,16);
    latitud=str2num(fgets(fid,6));
    fgetl(fid);
    fgets(fid,16);
    longitud=str2num(fgets(fid,6));
    frewind(fid);
    for i=1:83
        fgetl(fid);
    end
    A=fscanf(fid,'%f',[18,inf]);
    A=A';
    fclose(fid);
    m=[2*A(length(A)/2:end,5),2*A(length(A)/2:end,6)];
    M=round(m)/2+0.25;
    %clear A
    %clear aux
    %clear i
    %clear m
    P=[id, latitud, longitud];
    Hsmax=max(M(:,1))-0.25;
    Tmax=max(M(:,2))-0.25;
    TC=zeros(2*Hsmax,2*Tmax);
    for i=1:2*Hsmax
        for j=1:2*Tmax
            a=M(:,1)==i/2-0.25;
            b=M(:,2)==j/2-0.25;
            TC(i,j)=sum(a.*b)/530100;
        end
    end
    cabT=[0:0.5:Tmax];
    cabH=[0.5:0.5:Hsmax];
    cabH=cabH;
    TC=[cabH,TC];
    TC=[cabT;TC];
    clear a
    clear b
    fid=fopen('Hs_Tp.txt','w');
    B=size(TC);
    A=repmat(' %2.5f ',[1,B(2)]);
    A=[A,'\n'];
    fprintf(fid,'%7.0f %2.2f %1.3f\n',P);
    fprintf(fid,A,TC);
    fclose(fid);

    %Empiezo a convertir la TC en matriz más pequeñas para
    %multiplicarla por las matrices de potencia

    %Si la matriz de potencia tiene valores que la climatológica no, estos
    %deben eliminarse.

    if   TC(1,end)<limites(:,2)
       limites(:,2)=TC(1,end);
    end
    if   TC(end,1)<limites(:,4)
       limites(:,4)=TC(end,1);
    end

    %conversi�n TC a matrices climatol�gicas NxM que abarque mi matriz de potencia
%%
    Mposicion=zeros(9,4);
    for i=1:9
       posicion=[];
       F_limites=limites(i,:);
       for j=1:2
           aux=find(TC(1,:)==F_limites(j));
           if   F_limites(j)>max(TC(1,:))
                F_limites(j)=max(TC(1,:));
                aux=find(TC(:,1)==F_limites(j));
                posicion=[posicion,aux];
                qu=1;
           else
                aux=find(TC(:,1)==F_limites(j));
                posicion=[posicion,aux];
                qu=0;
           end
           posicion=[posicion,aux];
       end
       for j=3:4
           if F_limites(j)>max(TC(:,1))
                F_limites(j)=max(TC(:,1));
                aux=find(TC(:,1)==F_limites(j));
                posicion=[posicion,aux];
                qu=1;
           else
                aux=find(TC(:,1)==F_limites(j));
                posicion=[posicion,aux];
                qu=0;
           end
       end
       Mposicion(i,:)=[posicion];
       clear posicion
    end

    %Esto se pone aqu� para corregir un error en la posici�n de las columnas

    Mpos=[Mposicion(:,3),Mposicion(:,4),Mposicion(:,1),Mposicion(:,2),];
    Mposicion=Mpos;


    Mpelamis=TC(Mposicion(1,1):Mposicion(1,2),Mposicion(1,3):Mposicion(1,4));
    Mseapower=TC(Mposicion(2,1):Mposicion(2,2),Mposicion(2,3):Mposicion(2,4));
    Mwavestar=TC(Mposicion(3,1):Mposicion(3,2),Mposicion(3,3):Mposicion(3,4));
    Moceantec=TC(Mposicion(4,1):Mposicion(4,2),Mposicion(4,3):Mposicion(4,4));
    Mppc=TC(Mposicion(5,1):Mposicion(5,2),Mposicion(5,3):Mposicion(5,4));
    Menergy_buoy=TC(Mposicion(6,1):Mposicion(6,2),Mposicion(6,3):Mposicion(6,4));
    Mceto=TC(Mposicion(7,1):Mposicion(7,2),Mposicion(7,3):Mposicion(7,4));
    Mseabed=TC(Mposicion(8,1):Mposicion(8,2),Mposicion(8,3):Mposicion(8,4));
    Moyster_energy=TC(Mposicion(9,1):Mposicion(9,2),Mposicion(9,3):Mposicion(9,4));
    Mpotencias={Mpelamis,Mseapower,Mwavestar,Moceantec,Mppc,Menergy_buoy,Mceto,Mseabed,Moyster_energy};

    %convierto la ultima fila para que sume los estados de la mar m�s potentes

    Mpelamis(end,:)=sum(TC(Mposicion(1,2):end,Mposicion(1,3):Mposicion(1,4)));
    Mseapower(end,:)=sum(TC(Mposicion(2,2):end,Mposicion(2,3):Mposicion(2,4)));
    Mwavestar(end,:)=sum(TC(Mposicion(3,2):end,Mposicion(3,3):Mposicion(3,4)));
    Moceantec(end,:)=sum(TC(Mposicion(4,2):end,Mposicion(4,3):Mposicion(4,4)));
    Mppc(end,:)=sum(TC(Mposicion(5,2):end,Mposicion(5,3):Mposicion(5,4)));
    Menergy_buoy(end,:)=sum(TC(Mposicion(6,2):end,Mposicion(6,3):Mposicion(6,4)));
    Mceto(end,:)=sum(TC(Mposicion(7,2):end,Mposicion(7,3):Mposicion(7,4)));
    Mseabed(end,:)=sum(TC(Mposicion(8,2):end,Mposicion(8,3):Mposicion(8,4)));
    Moyster_energy(end,:)=sum(TC(Mposicion(9,2):end,Mposicion(9,3):Mposicion(9,4)));

    %Ahora quito las cabeceras a las matrices de potencia

    PM2=PM;
    for i=1:9
       PM2{i}(1,:)=[];
       PM2{i}(:,1)=[];
             for j=3:4
                while length(PM2{i}(:,1))~=length(Mpotencias{i}(:,1)); %para 
                    %igualar los tama�os de las matrices a�adiendo ceros
                    PM2{i}(end,:)=[];
                end
          end
    end

    %por ultimo, hago sumaproducto de la matriz de clima por la matriz de potencia
    VPtot=[];
    for i=1:9
       Ptot=8.76*sum(sum(PM2{i}.*Mpotencias{i}));
       VPtot=[VPtot,Ptot];
    end

    %Ahora vamos a calcular el factor de potencia

    Fpot=VPtot./(maximo*8.76);


    %Ahora calculo la potencia contenida en el clima (no la que extraigo)

    ro=1024;
    g=9.81;
    PN=[];
     T=TC(1,2:end);
     Hs=TC(2:end,1);
    for i=1:length(T)
        for j=1:length(Hs)
            pot_nat=ro*g*g*T(i)*Hs(j)*Hs(j)/(64*pi);
            PN(j,i)=pot_nat;
        end
    end
    Potencia_oleaje=sum(sum(PN))*3600/1000000000000; %que es la potencia en TWh

    P=[P,VPtot,100*Fpot,Potencia_oleaje];
    Puntos=[Puntos;P];
    disp('SIMAR  latitud longit pelamis seapower wavestar oceantec ppc energy_buoy ceto seabed oyster FPpelamis FPseapower FPwavestar FPoceantec FPppc FPE_buoy FPceto FPseabed FPoyster Potencia')
    fprintf('%7.0f %2.3f %2.3f %4.3f %4.3f %3.3f %4.3f %3.3f %4.3f %2.3f %2.3f %3.3f %2.3f %1.3f %1.3f %1.3f %1.3f %2.3f %1.3f %1.3f %1.3f %1.5f\n',Puntos')
    L=num2str((100*k/length(documentos)));
    disp(strcat('Avance= ',L,' %'))
    limit=limites;
end
%fid=fopen(strcat('C:\Users\daniel\Desktop\SIG\GIS tfm\Modificados\Matlab\Puertos\Tabla.txt'),'w');
%fprintf(fid,'SIMAR  latitud longit pelamis seapower wavestar oceantec ppc energy_buoy ceto seabed oyster FPpelamis FPseapower FPwavestar FPoceantec FPppc FPE_buoy FPceto FPseabed FPoyster Potencia\r\n')
%fprintf(fid,'%7.0f %2.3f %2.3f %4.3f %4.3f %3.3f %4.3f %3.3f %4.3f %2.3f %2.3f %3.3f %2.3f %1.3f %1.3f %1.3f %1.3f %2.3f %1.3f %1.3f %1.3f %1.5\n',Puntos')
%fclose(fid)
type Tabla.txt