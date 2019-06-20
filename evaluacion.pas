{ estimado programador del futuro, si quieres hacer comentario de varias lineas
solo debes hacer {LO QUE QUIERA}
//Este no se debe mostrat
program primos;
uses wincrt;
var
  primo  :boolean;
  num,divisor:integer;
begin
   primo:=true;
   divisor:=2.4;
   writeln('<===Programa que Determina si un Número es Primo o No!!!?_+==>');
   writeln; writeln;
   write('Introduzca un número===> '); readln(num);
   writeln;writeln;
   while (divisor<num) and primo do
   begin
     if num mod divisor = 0 then
          primo:=false;
     divisor:= #divisor+1
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


function max(num1, num2: integer): integer;

var
   (* local variable declaration *)
   result: integer;

begin
   if (num1 > num2) then
      result := num1
   
   else
      result := num2;
   max := result;
end;