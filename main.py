import modificar_valores as mv
import crecimiento_neto as cn
import graficos as gr
import grafics as g
import s3 as s3

s3.descargar()

mv.modificar_valores()
cn.crecimiento_neto()
gr.graficos()
g.graf_uri()

s3.cargar()