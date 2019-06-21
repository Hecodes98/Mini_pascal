program Calculadora;
uses crt;

Var a,b,c:integer;
d : real ;

Begin
Writeln(' Geek calculator program to University of Jaen :) ');
Writeln(' ');
Writeln('Codigo suma: 1 ; Codigo resta: 2 ; Codigo multiplicacion: 3 ; Codigo division: 4');
Writeln('Introduce el primer numero');
Readln(a);
Writeln(' ');
Writeln('Introduce el segundo numero');
Readln(b);
Writeln(' ');
Writeln('Introduce el codigo de la operacion que deseas hacer: ');
Readln(c);
Writeln(' ');
d := a / b ;
If c=1 then begin
Writeln('La suma es: ',a);
readln;
end
else begin
If c=2 then begin
Writeln('La resta es: ',a);
readln;
end
else begin
If c=3 then begin
Writeln('La multiplicacion es: ',a);
readln;
end
else begin
if c=4 then begin
Writeln('El resultado de la division es: ',a);

readln;
                end
            end;

        end;
    end;
end.