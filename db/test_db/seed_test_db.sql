\c test_commsys


-- design

DELETE FROM design;

INSERT INTO design (design_id, created_at, last_updated, design_name, file_location, file_name)
VALUES
    (1, '2024-05-01 12:00:00', '2024-05-01 12:00:00', 'apple0001', '/design/apple', 'apple0001.csv'),
    (2, '2024-05-02 12:00:00', '2024-05-02 12:00:00', 'apple0002', '/design/apple', 'apple0002.csv'),
    (3, '2024-05-03 12:00:00', '2024-05-03 12:00:00', 'apple0003', '/design/apple', 'apple0003.csv'),
    (4, '2024-05-04 12:00:00', '2024-05-04 12:00:00', 'apple0004', '/design/apple', 'apple0004.csv'),
    (5, '2024-05-05 12:00:00', '2024-05-05 12:00:00', 'apple0005', '/design/apple', 'apple0005.csv');


SELECT * FROM design;