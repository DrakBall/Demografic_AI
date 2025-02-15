import modificar_valores as mv
import graficos as gr
import s3 as s3

s3.descargar()

mv.modificar_valores()
gr.graficos()

s3.cargar()