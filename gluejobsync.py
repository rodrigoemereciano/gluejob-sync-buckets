import boto3

dst_path = 'tbff20001_metrica/'
prefix_source = 'topics/metrica-capturada/'
s3 = boto3.resource('s3')
source_bucket = s3.Bucket('metricsdev-src-bucket')
destination_bucket = s3.Bucket('metricsdev-dst-bucket')
destination_keys = [object.key for object in destination_bucket.objects.all()]

# teste de listas de objetos
#lista_bucket_source = [object.key for object in source_bucket.objects.all()]
#print(lista_bucket_source)
#print(destination_keys)

# comparação de objects entre buckets e cópia de objetos
for object in source_bucket.objects.all():
    obj_destino = dst_path + object.key.removeprefix(prefix_source)
    obj_semprefixo = object.key.removeprefix(prefix_source)
    if ( obj_destino not in destination_keys):
        copy_source = {
            'Bucket': 'metricsdev-src-bucket',
            'Key': object.key
        }
        print('nao tem o objeto: ', obj_semprefixo)
        destination_bucket.copy(copy_source, obj_destino)
    print('já existe o objeto: ', obj_semprefixo)


# comparação de objetos se existem ----> OK
# cópia de objetos se não existirem ----> OK
# copiar objetos sem prefixo de diretório de origem ---> OK