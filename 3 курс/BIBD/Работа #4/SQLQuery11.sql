-- �������� ��������� ��� ������� ����� ������:

CREATE PROCEDURE InsertFirm
    @firm NVARCHAR(255),
    @addr NVARCHAR(255),
    @tel NVARCHAR(15)
AS
BEGIN
    INSERT INTO [�����] ([�����], [�����], [�������])
    VALUES (@firm, @addr, @tel)
END