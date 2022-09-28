import boto3

destination_path = 'tbff20001_metrica/metricas/'
prefix_path_source = 'anomesdia=20220927/'
s3 = boto3.resource('s3')
source_bucket = s3.Bucket('metricsdev-src-bucket')
destination_bucket = s3.Bucket('metricsdev-dst-bucket')
destination_keys = [object.key for object in destination_bucket.objects.all()]

# teste de listas de objetos
lista_bucket_source = [object.key for object in source_bucket.objects.all()]
print(lista_bucket_source)
print(destination_keys)

# comparação de objects entre buckets e cópia de objetos
for object in source_bucket.objects.all():
  if ( destination_path+object.key.removeprefix(prefix_path_source) not in destination_keys):
    copy_source = {
        'Bucket': 'metricsdev-src-bucket',
        'Key': object.key
    }
    print('nao tem o objeto: ', object.key.removeprefix(prefix_path_source))
    destination_bucket.copy(copy_source, destination_path+object.key.removeprefix(prefix_path_source))
  print('já existe o objeto: ', object.key.removeprefix(prefix_path_source))


# comparação de objetos se existem ----> OK
# cópia de objetos se não existirem ----> OK
# copiar objetos sem prefixo de diretório de origem ---> OK