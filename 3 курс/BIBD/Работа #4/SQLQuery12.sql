USE [Услуги]
GO
/****** Object:  UserDefinedFunction [dbo].[GetFirmInfoByTel]    Script Date: 17.10.2023 9:49:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER FUNCTION [dbo].[GetFirmInfoByTel] (@FirmTel nchar(15))
RETURNS TABLE
AS
RETURN (
    SELECT [Фирма], [Адрес], [Телефон]
    FROM [Фирмы]
    WHERE [Телефон] = @FirmTel
)