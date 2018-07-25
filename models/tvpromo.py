# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions,_
from odoo.osv import osv
from datetime import time,datetime,date,timedelta
#from stdnum.mx.rfc import (validate,InvalidComponent,InvalidFormat,InvalidLength,InvalidChecksum)

GRADO_ESTUDIOS_ESCOLARIDAD=[
    ('P1','Preescolar'),
    ('P2','Primaria'),
    ('S1','Secundaria'),
    ('P3','Preparatoria'),
    ('M1','Media Superior'),
    ('S2','Superior'),
    ('M2','Maestria'),
    ('D','Doctorado'),
]

ESTADO_ESTUDIOS_ESCOLARIDAD=[
    ('I','Inscrito'),
    ('C','Cursando'),
    ('F','Finalizado'),
]

MOTIVO_CONTRATO=[
    ('A','Aumento de sueldo'),
    ('C1','Cambio de puesto'),
    ('R1','Renovacion'),
    ('V','Vencimiento'),
    ('R2','Recorte de personal'),
    ('C2','Cancelacion de contrato'),
]

TIPO_SANGRE_EMPLEADO=[
    ('O-','O Negativo'),
    ('O+','O Positivo'),
    ('A-','A Negativo'),
    ('A+','A Positivo'),
    ('B-','B Negativo'),
    ('B+','B Positivo'),
    ('AB-','AB Negativo'),
    ('AB+','AB Positivo'),
]

TIPO_SEGURO_SEGUROS_VARIOS=[
    ('SV','Vida'),
    ('SGM','Gastos Medicos Mayores'),
    ('SDV','Viaje'),
    ('OS','Otro Seguro')
]

MONEDA_SEGUROS_SEGUROS_VARIOS=[
    ('MXN','Moneda Nacional.'),
    ('DLL','Dolares'),
    ('EUROS','Euros'),
]

RESPUESTAS_ZAVIC=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
]

class tvp_escolaridad(models.Model):
    _name='tvp.escolaridad'

    nombre=fields.Char('Nombre del Estudio',required=True)
    empleado=fields.Many2one('hr.employee','Empleado',required=True)
    nivel_de_estudio=fields.Selection(GRADO_ESTUDIOS_ESCOLARIDAD,'Nivel de Estudio',required=True)
    estado_estudio=fields.Selection(ESTADO_ESTUDIOS_ESCOLARIDAD,'Estado del Estudio',required=True)
    nombre_escuela_estudio=fields.Char('Nombre de la escuela',required=True)
    constancia_recibida=fields.Char('Documento Oficial',required=True)
    notas=fields.Text('Notas::Obs.',size=30)


class tvp_contrato(models.Model):
    _name='tvp.contrato'

    activo=fields.Boolean('Contrato activo',default=True,required=True)
    meses_prestaciones=fields.Float('Prestacones en meses',required=True)
    sueldo_bruto_mensual=fields.Float('SBM',help='Sueldo bruto mensual',required=True)
    sueldo_bruto_anual=fields.Float('SBA',help='Sueldo bruto anual',required=True)
    nivel_de_puesto=fields.Many2one('nivel_de_puesto','Nivel de puesto',index=True,requierd=True)
    base_anual=fields.Many2one('base_anual','Base anual',index=True,requierd=True)
    compania_contratadora=fields.Many2one('res.company','Empresa',index=True)
    motivo=fields.Selection(MOTIVO_CONTRATO,'Motivo',required=True)
    porcentaje=fields.Float('%',required=True,help='Porcentaje aumentado')
    nuevo_sueldo=fields.Float('Nuevo sueldo bruto',help='Monto del sueldo nuevo')
    monto_finiquito=fields.Float('Monto finiquitado',help='En caso de liquidacion o finiquito')
    obs=fields.Text('Obs./Notas',size=30)

class nivel_puesto(models.Model):
    _name='nivel.puesto'
    nombre=fields.Char('Nivel de puesto', required=True)
    obs=fields.Text('Obs./Notas',size=30,required=True)

class base_anual(models.Model):
    _name='base.anual'
    nombre=fields.Char('Base anual', required=True)
    obs=fields.Text('Obs./Notas',size=30,required=True)



class tvp_empleado(models.Model):
    _name='tvp.empleado'

    rfc=fields.Char(string='R.F.C.',size=13,required=True)
    nss=fields.Char(string='N.S.S.',size=11,required=True)
    nom_contacto=fields.Char('Nombre del contacto')
    tel_contacto=fields.Char('Tel. de contacto',size=10)
    fecha_ingreso=fields.Date('Fecha de ingreso',default=date.today())
    antiguedad=fields.Char('Antiguedad',size=2)
    edad=fields.Char('Edad',size=2,required=True)
    tipo_sangre=fields.Selection(TIPO_SANGRE_EMPLEADO,'Tipo de sangre',required=True)
    num_empleado=fields.Integer('Numero de empleado',required=True)
    fecha_baja=fields.Date('Fecha de baja',help='Si lo requiere llene este campo con la fecha correspondiente a la baja...')


    #@api.multi
    #def validate_rfc(self):
    #    if self.rfc=="XEXX010101000" or self.rfc=="XAXX010101000":
    #        return True
    #    else:
    #        try:
    #            retorno=validate(self.rfc,validate_check_digits=True)
    #            return True
    #        except:
    #            raise osv.except_osv(('¡Error!'),('El RFC no es valido, Verificar...'))
                #raise exceptions.except_orm(_('Error'),_('RFC no VALIDO'))


class tvp_gas(models.Model):
    _name='tvp.gas'

    activa = fields.Boolean('Activa',default=True,required=True )
    num_tarjeta=fields.Char('Numero de tarjeta',required=True,size=16)
    empleado=fields.Many2one('hr.employee','Empleado',required=True)
    departamento=fields.Many2one('hr.department','Departamento',required=True)
    puesto=fields.Many2one('hr.job','Pues que desempeña',required=True)
    monto_mensual=fields.Float('Monto mensual',required=True )
    proveedor=fields.Many2one('res.partner','Proveedor',required=True)
    obs=fields.Text('Obs./Notas',size=30)


class tvp_seguros(models.Model):
    _name='tvp.seguros'

    activa = fields.Boolean('Activa',default=True,required=True )
    clave=fields.Char('Clave del seguro',required=True)
    empleado=fields.Many2one('hr.employee','Empleado',required=True)
    departamento=fields.Many2one('hr.department','Departamento',required=True)
    puesto=fields.Many2one('hr.job','Pues que desempeña',required=True)
    tipo_seguro=fields.Selection(TIPO_SEGURO_SEGUROS_VARIOS,'Tipo de seguro',required=True,help='Selecciona segun corresponda.')
    tipo_moneda=fields.Selection(MONEDA_SEGUROS_SEGUROS_VARIOS,'Tipo de moneda',required=True,help='Seleccciona el tipo de cambio')
    prima_neta =fields.Float('Prima neta mensual',required=True,help='Monto mensual de la tarjeta o seguro')
    vigencia=fields.Integer("Vigencia (meses)",required=True,size=2,default=12)
    fecha_ingreso=fields.Date('Fecha de inicio',default=date.today())
    fecha_vencimiento=fields.Date('Fecha de vencimiento',required=True)
    obs=fields.Text('Obs./Notas',size=30,help='Anota la descripcion del seguro y otras notas...')


class tvp_zavic(models.Model):
    _name='tvp.zavic'

    pregunta=fields.Char('Pregunta',required=True,help='Responde la pregunta segun corresponda')
    respuesta=fields.Selection(RESPUESTAS_ZAVIC,'Respuesta',required=True,help='Selecciona la respuesta correcta')
