def pstFilesSave(
        ID,
        Name,
        FileCategory,
        fuvStartDate,
        fuvEndDate,
        fuvType,
        fuvTradeDate,
        fuvProcessingOrder,
        fuvPart,
        fuvTemplateNameDC,
        fuvTemplateChangeDate,
        Status,
        CreateDate,
        LoadedToStagingDate,
        LoadedToCoreDate
):

    logging.info('Начало загрузки данных в таблицу stFiles')

    try: 

        cnxn = pyodbc.connect('DRIVER=' + config.driver +
                             ';SERVER=' + config.server +
                             ';DATABASE=' + config.database +
                             ';UID=' + config.username +
                             ';PWD=' + config.password
                            )

        if fuvStartDate != 'NULL':
            fuvStartDate = datetime.strptime(fuvStartDate, '%d.%m.%Y %H:%M:%S')
        if fuvEndDate != 'NULL':
            fuvEndDate = datetime.strptime(fuvEndDate, '%d.%m.%Y %H:%M:%S')
        if fuvTradeDate != 'NULL':
            fuvTradeDate = datetime.strptime(fuvTradeDate, '%d.%m.%Y %H:%M:%S')

        if fuvTemplateChangeDate != 'NULL':
            fuvTemplateChangeDate = datetime.strptime(fuvTemplateChangeDate, '%d.%m.%Y %H:%M:%S')

        if CreateDate != 'NULL':
            CreateDate = datetime.strptime(CreateDate, '%d.%m.%Y %H:%M:%S')

        if LoadedToStagingDate != 'NULL':
            LoadedToStagingDate = datetime.strptime(LoadedToStagingDate, '%d.%m.%Y %H:%M:%S')

        if LoadedToCoreDate != 'NULL':
            LoadedToCoreDate = datetime.strptime(LoadedToCoreDate, '%d.%m.%Y %H:%M:%S')
       
        values = (
            ID,
            Name,
            int(FileCategory),
            fuvStartDate,
            fuvEndDate,
            int(fuvType),
            fuvTradeDate,
            fuvProcessingOrder,
            fuvPart,
            fuvTemplateNameDC,
            fuvTemplateChangeDate,
            Status,
            CreateDate,
            LoadedToStagingDate,
            LoadedToCoreDate
        )
 
        cursor = cnxn.cursor()

        cursor.execute("{CALL dbo.pstFilesSave(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}", values)

        for row in cursor:

            print(row)

    except pyodbc.Error as e:

        logging.error(f'Ошибка: {e}')

     finally:

        cnxn.close()