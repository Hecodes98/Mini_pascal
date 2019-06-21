Program Primo; 
uses crt; 
var 
   cont, num, i : integer; 
begin 
   readln(num); 
   cont:=0; 
   for i:=1 to num do 
    begin
      if num mod i = 0 then 
   cont:=cont+1; 
   if cont = 2 then 
      writeln('Es primo...');
   else 
      writeln('No es primo...'); 
   readln; 
   end;
end.