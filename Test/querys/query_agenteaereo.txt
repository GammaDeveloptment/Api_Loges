select   cast(C.fechasolicitudreserva as date) as reserva,C.fechaingresoalmacen ,

a.CodigoAerolinea ,a.ReferenciaInternoGuiaAereA,C.numerointernoguiahija,A.FECHAREALSALIDA,A.FECHAREALLLEGADA, 

              SM.Nombre AS Shipper_Master, SM.Direccion AS DireccionShipper_Master,SM.TelefonoCentral AS TelefonoCentral_master ,

              SM.NUMERODOCUMENTO AS RUC_SHIPPER_MASTER, SME.NombrePais AS PaisShipper_MASTER, SMF.NombreCiudad AS CiudadShipper_MASTER, 

              CM.Nombre AS Consignee_MASTER, CM.Direccion AS DireccionConsignee_MASTER,CM.TelefonoCentral as TelefonoCentralC_MASTER ,

              CM.NUMERODOCUMENTO AS RUC_CONSIGNEE_MASTER ,CMh.NombrePais AS PaisConsignee_MASTER, CMi.NombreCiudad AS CiudadConsignee_MASTER,

              d.Nombre AS Shipper, d.Direccion AS DireccionShipper,D.TelefonoCentral,D.NUMERODOCUMENTO AS RUC_SHIPPER, e.NombrePais AS PaisShipper,

              f.NombreCiudad AS CiudadShipper,  

              g.Nombre AS Consignee, g.Direccion AS DireccionConsignee,g.TelefonoCentral as TelefonoCentralC ,G.NUMERODOCUMENTO AS RUC_CONSIGNEE ,

              a.NumeroGuiaMaster, b.Nombre AS Aerolinea,  a.NumeroVuelo, 

              x.NombrePais AS PaisCarga,Y.CODIGOCIUDAD AS CODIGO_CARGA, y.NOMBRECIUDAD AS CiudadCarga, z.NombrePais AS PaisDescarga,

              W.CODIGOCIUDAD AS CODIGO_DESCARGA, w.NOMBRECIUDAD AS PuertoDescarga, 

              c.NumeroGuiaHija AS NumeroGuia, c.TipoCondicionFlete,h.NombrePais AS PaisConsignee, i.NombreCiudad AS CiudadConsignee,  

              C.CantidadBultos, C.DescripcionMercaderia, C.PesoBruto,C.PesoVolumen    

              FROM GuiaMasterAerea a LEFT JOIN GuiaHijaAerea c ON c.ReferenciaInternoGuiaAerea=a.ReferenciaInternoGuiaAerea  

              LEFT JOIN EmpresaTransporte b ON b.CodigoEmpresaTransporte=a.codigoaerolinea AND b.TipoEmpresaTransporte='A'  

              LEFT JOIN Pais x   ON x.CodigoPais=SUBSTR(a.CODIGOAEROPUERTOORIGEN,1,2)   

              LEFT JOIN Ciudad y ON y.CodigoCiudad=SUBSTR(a.CODIGOAEROPUERTOORIGEN,3,3) AND y.CodigoPais=SUBSTR(a.CODIGOAEROPUERTOORIGEN,1,2)   

              LEFT JOIN Pais Z   ON Z.CodigoPais=SUBSTR(a.CODIGOAEROPUERTODESTINO,1,2)

              LEFT JOIN CIUDAD w ON w.CodigoCiudad=SUBSTR(a.CODIGOAEROPUERTODESTINO,3,3) AND w.CodigoPais=SUBSTR(a.CODIGOAEROPUERTODESTINO,1,2)

              LEFT JOIN Persona SM ON SM.CodigoPersona=A.CodigoShipper   

              LEFT JOIN Pais SME    ON SME.CodigoPais=SM.CodigoPais   

              LEFT JOIN Ciudad SMF  ON SMF.CodigoCiudad=SM.CodigoCiudad AND SMF.CodigoPais=SM.CodigoPais  

              LEFT JOIN Persona CM ON CM.CodigoPersona=A.CodigoConsignee   

              LEFT JOIN Pais CMh    ON CMh.CodigoPais=CM.CodigoPais    

              LEFT JOIN Ciudad CMi  ON CMi.CodigoCiudad=CM.CodigoCiudad AND CMi.CodigoPais=CM.CodigoPais  

              LEFT JOIN Persona d ON d.CodigoPersona=c.CodigoShipper  

              LEFT JOIN Pais e    ON e.CodigoPais=d.CodigoPais   

              LEFT JOIN Ciudad f  ON f.CodigoCiudad=d.CodigoCiudad AND f.CodigoPais=d.CodigoPais  

              LEFT JOIN Persona g ON g.CodigoPersona=c.CodigoConsignee  

              LEFT JOIN Pais h    ON h.CodigoPais=g.CodigoPais  

              LEFT JOIN Ciudad i  ON i.CodigoCiudad=g.CodigoCiudad AND i.CodigoPais=g.CodigoPais  

 Where a.fechaemision>='20240101' and a.estado<>'E' and C.estado<>'E' and a.tipooperacion='E'  and  ( a.fecharealsalida isnull or

   cast(a.fecharealsalida as date) >= cast(current_date as date)-3 and  cast(a.fecharealsalida as date) <=cast(current_date as date)+2 )

and a.codigoconsignee='numero_agente'