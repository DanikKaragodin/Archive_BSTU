-- �������� ������� ��� ��������� ���������� � ����� �� � ��������:
CREATE FUNCTION GetFirmInfoByTel (@FirmTel INT)
RETURNS TABLE
AS
RETURN (
    SELECT [�����], [�����], [�������]
    FROM [�����]
    WHERE  [�������] = @FirmTel
)