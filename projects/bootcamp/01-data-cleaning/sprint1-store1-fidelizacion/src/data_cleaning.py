"""
Módulo para limpieza y transformación de datos de clientes
"""


def limpiar_usuarios(usuarios):
    """
    Estandariza los nombres de usuarios. 
    """
    usuarios_limpios = []
    
    for usuario in usuarios:        
        usuario_id, nombre, edad, categorias, gastos = usuario       
        
        # Convertir usuario_id en entero
        usuario_id_nuevo = int(usuario_id)
        
        # Limpiar nombre: quitar espacios de cadena
        nombre_limpio = nombre.strip()
        # Reemplazar el guion bajo por espacio
        nombre_limpio = nombre_limpio.replace('_',' ')
        # Estandarizar los nombres en minúsculas      
        nombre_limpio = nombre_limpio.lower()
        # Dividir en nombre y apellido
        name_s = nombre_limpio.split(' ')
        nombre_limpio = name_s[0]
        apellido_limpio = name_s[1]
        
        # Estandarizar las categorias en minusculas
        categorias_estandarizadas = [cat.lower() for cat in categorias]
        edad_limpia = int(edad)        
        
        
        usuario_limpio = [
            usuario_id_nuevo,
            nombre_limpio,
            apellido_limpio,
            edad_limpia,
            categorias_estandarizadas,
            gastos
        ]
        usuarios_limpios.append(usuario_limpio)    
        
        
    return usuarios_limpios

def test_try(usuarios):
    
    for usuario in usuarios:        
        usuario_id, nombre, apellido, edad, categorias, gastos = usuario
        
        # Convertir el valor de la edad a numero entero, considerando valores que no sean número
        try:
            edad_limpia = int(edad)
        except:
            print ('Please provide your age as a numerical value')
    
    
def calcular_gasto_total(usuarios):
    """
    Calcula el gasto total por cliente
    """
    usuarios_con_gasto = []
    
    for usuario in usuarios:
        usuario_id, nombre, apellido, edad, categorias, gastos = usuario
        gasto_total = sum(gastos)
        
        usuario_con_gasto = usuario + [gasto_total]
        usuarios_con_gasto.append(usuario_con_gasto)
        
    
    return usuarios_con_gasto
    
def pipeline_limpieza_completa(usuarios):
    """
    Ejecuta todo el pipeline de limpieza y transformación
    """
    print("Iniciando pipeline de limpieza...")
    
    usuarios_limpios = limpiar_usuarios(usuarios)
    print("✓ Nombres limpiados")    
    
    usuarios_limpios = calcular_gasto_total(usuarios_limpios)
    print("✓ Gasto total calculado")
    
    print("Pipeline de limpieza completado!")
    return usuarios_limpios

# Bloque de pruebas SOLO si se ejecuta directamente
'''
if __name__ == "__main__":
    users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
    ]
    
    usuarios = pipeline_limpieza_completa(users)
    for usuario in usuarios:
        print(usuario)
'''