-- Хранимая функция для получения информации о фирме по её ID:

CREATE FUNCTION GetFirmInfoByTel (@FirmTel INT)
RETURNS TABLE
AS
RETURN (
    SELECT [Фирма], [Адрес], [Телефон]
    FROM [Фирмы]
    WHERE [Телефон] = @FirmTel
)