-- Хранимая процедура для вставки новой записи:

CREATE PROCEDURE InsertFirm
    @firm NVARCHAR(255),
    @addr NVARCHAR(255),
    @tel NVARCHAR(15)
AS
BEGIN
    INSERT INTO [Фирмы] ([Фирма], [Адрес], [Телефон])
    VALUES (@firm, @addr, @tel)
END