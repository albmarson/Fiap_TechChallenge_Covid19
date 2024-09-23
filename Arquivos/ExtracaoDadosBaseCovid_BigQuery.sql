select 
-- dados gerais
    m.ano as ano,
    m.mes as mes,
    m.semana as semana,
    e.nome as estado,
    TRANSLATE(
    e.nome,
    '¡…Õ”⁄¿»Ã“Ÿ¬ Œ‘€√’«·ÈÌÛ˙‡ËÏÚ˘‚ÍÓÙ˚„ıÁ',
    'AEIOUAEIOUAEIOUAOCaeiouaeiouaeiouaoc'
  ) AS estado_sem_acento,
    d1.valor as urbano_rural,
    m.a002    as  idade   ,
    d4.valor    as  sexo    ,
    d5.valor    as  cor_raca    ,
-- sintomas
    d50.valor as restricao_contato,
    d7.valor    as  febre,
    d8.valor    as  tosse,
    d9.valor    as  dor_de_garganta,
    d10.valor   as  dificuldade_respirar,
    d11.valor   as  dor_de_cabeca,
    d12.valor   as  dor_no_peito,
    d13.valor   as  nausea,
    d14.valor   as  nariz_entupido_escorrendo,
    d15.valor   as  fadiga,
    d16.valor   as  dor_nos_olhos,
    d17.valor   as  perda_cheiro_sabor,
    d18.valor   as  dor_muscular,
    d19.valor   as  diarreia,
    case
        when 'Sim' in (d7.valor, d8.valor, d9.valor, d10.valor, d11.valor, d12.valor, d13.valor, d14.valor, d15.valor, d16.valor, d17.valor, d18.valor, d19.valor) then 'Sim'
        else 'N„o'
    end as teve_sintomas,
 case
        when 'Sim' in (d7.valor, d8.valor, d9.valor, d10.valor, d11.valor, d12.valor, d13.valor, d14.valor, d15.valor, d16.valor, d17.valor, d18.valor, d19.valor) then 
            (case
                when d7.valor = 'Sim' then 1 else 0 end +
            case
                when d8.valor = 'Sim' then 1 else 0 end +
            case
                when d9.valor = 'Sim' then 1 else 0 end +
            case
                when d10.valor = 'Sim' then 1 else 0 end +
            case
                when d11.valor = 'Sim' then 1 else 0 end +
            case
                when d12.valor = 'Sim' then 1 else 0 end +
            case
                when d13.valor = 'Sim' then 1 else 0 end +
            case
                when d14.valor = 'Sim' then 1 else 0 end +
            case
                when d15.valor = 'Sim' then 1 else 0 end +
            case
                when d16.valor = 'Sim' then 1 else 0 end +
            case
                when d17.valor = 'Sim' then 1 else 0 end +
            case
                when d18.valor = 'Sim' then 1 else 0 end +
            case
                when d19.valor = 'Sim' then 1 else 0 end)
        else 0
    end as num_sintomas,
-- atendimento
    d20.valor as procurou_atendimento,
    d28.valor as atendimento_ubs,
    d29.valor as atendimento_pa_sus,
    d30.valor as atendimento_hospital_sus,
    d31.valor as atendimento_consultorio_privado,
    d32.valor as atendimento_ps_privado,
    d33.valor as atendimento_hospital_privado,
case
        when d20.valor = 'Sim' and 'Sim' in (d30.valor, d33.valor) then 'Buscou hospital'
        when d20.valor = 'N„o' or d20.valor is null then 'N„o buscou atendimento'
        else 'Outras formas de atendimento'
    end as forma_atendimento,
    d34.valor as ficou_internado,
    d35.valor as foi_entubado,
    d36.valor as tem_plano_saude,
-- teste covid
    d37.valor as fez_teste_covid,
    case
        when d37.valor = 'Sim' and 'Positivo' in (d39.valor, d41.valor, d43.valor) then 'Positivo'
        else 'Negativo'
    end as resultado_teste_covid,
-- financeiro
    d51.valor as trabalhou,
    d54.valor as ctps_assinada,
    d71.valor as contribui_inss,
    d52.valor as afasamento_trabalho,
    m.c01012 as valor_renda,
    m.d0013 as valor_aposentadoria,
    m.d0023 as valor_pensao,
    m.d0033 as valor_bolsa_familia,
    m.d0043 as valor_beneficios,
    m.d0053 as valor_auxilios,
    m.d0063 as valor_seguro_desemprego,
    m.d0073 as valor_outros_rendimentos,
    coalesce(m.c01012, 0) + coalesce (m.d0013, 0) + coalesce (m.d0023, 0) +
    coalesce (m.d0033, 0) + coalesce (m.d0043, 0) + coalesce (m.d0053, 0) +
    coalesce (m.d0063, 0) + coalesce (m.d0073, 0) as soma_rendimentos,
    d65.valor as emprestimo,
    d70.valor as casa_propria_alugada_outros
from
    `basedosdados.br_ibge_pnad_covid.microdados` as m
-- cruzamento com outras bases/dicion·rio
    left join   `basedosdados.br_bd_diretorios_brasil.uf`    as e on m.sigla_uf = e.sigla
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as d1 on m.v1022 = cast(d1.chave as string) and d1.nome_coluna = 'v1022'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d4  on  m.a003 =    cast(   d4.chave    as  string  )   and d4.nome_coluna =    'a003'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d5  on  m.a004 =    cast(   d5.chave    as  string  )   and d5.nome_coluna =    'a004'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d7  on  m.b0011 =   cast(   d7.chave    as  string  )   and d7.nome_coluna =    'b0011'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d8  on  m.b0012 =   cast(   d8.chave    as  string  )   and d8.nome_coluna =    'b0012'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d9  on  m.b0013 =   cast(   d9.chave    as  string  )   and d9.nome_coluna =    'b0013'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d10 on  m.b0014 =   cast(   d10.chave   as  string  )   and d10.nome_coluna =   'b0014'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d11 on  m.b0015 =   cast(   d11.chave   as  string  )   and d11.nome_coluna =   'b0015'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d12 on  m.b0016 =   cast(   d12.chave   as  string  )   and d12.nome_coluna =   'b0016'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d13 on  m.b0017 =   cast(   d13.chave   as  string  )   and d13.nome_coluna =   'b0017'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d14 on  m.b0018 =   cast(   d14.chave   as  string  )   and d14.nome_coluna =   'b0018'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d15 on  m.b0019 =   cast(   d15.chave   as  string  )   and d15.nome_coluna =   'b0019'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d16 on  m.b00110 =  cast(   d16.chave   as  string  )   and d16.nome_coluna =   'b00110'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d17 on  m.b00111 =  cast(   d17.chave   as  string  )   and d17.nome_coluna =   'b00111'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d18 on  m.b00112 =  cast(   d18.chave   as  string  )   and d18.nome_coluna =   'b00112'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d19 on  m.b00113 =  cast(   d19.chave   as  string  )   and d19.nome_coluna =   'b00113'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d20 on  m.b002 =    cast(   d20.chave   as  string  )   and d20.nome_coluna =   'b002'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d28 on  m.b0041 =   cast(   d28.chave   as  string  )   and d28.nome_coluna =   'b0041'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d29 on  m.b0042 =   cast(   d29.chave   as  string  )   and d29.nome_coluna =   'b0042'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d30 on  m.b0043 =   cast(   d30.chave   as  string  )   and d30.nome_coluna =   'b0043'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d31 on  m.b0044 =   cast(   d31.chave   as  string  )   and d31.nome_coluna =   'b0044'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d32 on  m.b0045 =   cast(   d32.chave   as  string  )   and d32.nome_coluna =   'b0045'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d33 on  m.b0046 =   cast(   d33.chave   as  string  )   and d33.nome_coluna =   'b0046'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d34 on  m.b005 =    cast(   d34.chave   as  string  )   and d34.nome_coluna =   'b005'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d35 on  m.b006 =    cast(   d35.chave   as  string  )   and d35.nome_coluna =   'b006'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d36 on  m.b007 =    cast(   d36.chave   as  string  )   and d36.nome_coluna =   'b007'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d37 on  m.b008 =    cast(   d37.chave   as  string  )   and d37.nome_coluna =   'b008'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d39 on  m.b009b =   cast(   d39.chave   as  string  )   and d39.nome_coluna =   'b009b'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d41 on  m.b009d =   cast(   d41.chave   as  string  )   and d41.nome_coluna =   'b009d'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d43 on  m.b009f =   cast(   d43.chave   as  string  )   and d43.nome_coluna =   'b009f'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d50 on  m.b011 =    cast(   d50.chave   as  string  )   and d50.nome_coluna =   'b011'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d51 on  m.c001 =    cast(   d51.chave   as  string  )   and d51.nome_coluna =   'c001'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d52 on  m.c002 =    cast(   d52.chave   as  string  )   and d52.nome_coluna =   'c002'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d54 on  m.c007b =   cast(   d54.chave   as  string  )   and d54.nome_coluna =   'c007b'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d65 on  m.e001 =    cast(   d65.chave   as  string  )   and d65.nome_coluna =   'e001'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d70 on  m.f001 =    cast(   d70.chave   as  string  )   and d70.nome_coluna =   'f001'
    left join   `basedosdados.br_ibge_pnad_covid.dicionario` as     d71 on  m.c014 =    cast(   d71.chave   as  string  )   and d71.nome_coluna =   'c014'
-- seleÁ„o do perÌodo de 3 meses para consulta
where
    mes between 7 and 9