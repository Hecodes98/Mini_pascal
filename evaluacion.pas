{ Programa que determina si un número N es primo. (Un número primo sólo
  puede ser divisible por el mismo y la unidad...compilado en
  en Borland Pascal para Windows Version 7.0}
program primos;
uses wincrt;
var
  primo  :boolean;
  num,divisor:integer;
begin
   primo:=true;
   divisor:=2;
   writeln('<===Programa que Determina si un Número es Primo o No===>');
   writeln; writeln;
   write('Introduzca un número===> '); readln(num);
   writeln;writeln;
   while (divisor<num) and primo do
   BEGIN
     if num mod divisor = 0 then
          primo:=false;
     divisor:=divisor+1
   end;
 if primo = true then
    writeln(num,' Es número Primo...')
 else
    writeln(num,' No es un número Primo...');
 writeln;
 writeln;
 writeln('Diseñado por: Victor Manuel Evaristo Salinas');
 writeln;
 writeln;
 writeln('E-mail: victor_mes@hotmail.com y vmanuel_es@yahoo.com.mx');
 writeln;
end.