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
   writeln;writeln;
   while (divisor<num) and primo do
   begin
     if num mod divisor = true and 1<divisor then
          primo:=false;
     divisor:= divisor+1;
   end;
 if primo = true then
    writeln(' Es número Primo...');
 else
    writeln(' No es un número Primo...');
 writeln;
 writeln;
 writeln('Diseñado por: Victor Manuel Evaristo Salinas');
 writeln;
 writeln;
 writeln('E-mail: victor_mes@hotmail.com y vmanuel_es@yahoo.com.mx');
 writeln;
end.

//dadjasjdasd
