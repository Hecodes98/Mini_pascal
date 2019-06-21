program recursivo;
   uses
     crt;
 
   var
     tecla : char;
     salir : boolean;
     cuenta : integer;
 
 
     function potenciarecursiva(m : real; n : integer) : real;
     Begin
        if n = 0 then
        potenciarecursiva := 1.0;
    else
       potenciarecursiva := potenciarecursiva(m, n - 1);
    End;
 
 
   procedure LAPOTENCIARECURSIVA;
   var
     rel : real;
     ent : integer;
   begin
       writeln('   Entre Numero Real   : ');
       readln(rel);
       writeln('   Entre Numero Entero : ');
       readln(ent);
       writeln('   La Potencia Es : ',potenciarecursiva(rel, ent));
       readln;
   end;
 
 
   function MAXIMOCOMUNDIVISORRECURSIVO(nn, kk : integer) : integer;
   var
    max, min : integer;
   begin
      If nn > kk Then
        Begin
          max := nn;
          min := kk;
        End
      Else
        Begin
          max := kk;
          min := nn;
        End;
         If nn = 0 Then
         MAXIMOCOMUNDIVISORRECURSIVO := kk;
  end;
 
   function defectuoso(num, p : integer) : boolean;
   begin
      if p > 1  then
      begin
       if frac(num / p) = 0 then
       begin
       cuenta := cuenta + (num div p);
       write('  ',trunc(num / p));
       end;
       defectuoso := defectuoso(num, p - 1);
      end
    else
      begin
      cuenta := cuenta;
      if cuenta <> num then
      defectuoso := true
    else
      defectuoso := false;
      write('  ');
      exit;
      end;
   end;
 
 
   procedure NUMERODEFECTUOSO;
   var
      nu : integer;
   begin
      write('   Entre Numero Entero : ');
      readln(nu);
      cuenta := 0;
      writeln('   El Numero es = ',defectuoso(nu,nu));
      writeln('  Entrado = ',nu,'   Respuesta = ',cuenta);
      readkey;
   end;
 
 
 
   procedure menu;
   var
     s, g : longint;
   begin
      salir := false;
   end;
 
 
   begin
      menu;
   end.