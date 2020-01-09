CREATE DATABASE replacement_handsets_test /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION=N */;

USE replacement_handsets_test
GO
CREATE TABLE handsetorders_table
(
    order_id int NOT NULL PRIMARY KEY,
    site_ID varchar(10) DEFAULT NULL,
    handset_model varchar(50) DEFAULT NULL,
    part_number varchar(50) DEFAULT NULL,
    fault_description varchar(300) DEFAULT NULL,
    quantity int DEFAULT NULL,
    contact_name varchar(50) DEFAULT NULL,
    contact_number varchar(20) DEFAULT NULL,
    contact_email varchar(50) DEFAULT NULL,
    delivery_address varchar(100) DEFAULT NULL
);

USE replacement_handsets_test
GO
CREATE PROCEDURE new_order(
    @new_siteID AS VARCHAR(10),
    @new_handsetModel AS VARCHAR(50),
    @new_partNumber AS VARCHAR(50),
    @new_faultDesc AS VARCHAR(300),
    @new_quantity AS INTEGER,
    @new_contactName AS VARCHAR(50),
    @new_contactNumber AS VARCHAR(20),
    @new_contactEmail AS VARCHAR(50),
    @new_deliveryAddress AS VARCHAR(100)
)
AS
BEGIN
    INSERT INTO handsetorders_table
        (
        site_ID,
        handset_model,
        part_number,
        fault_description,
        quantity,
        contact_name,
        contact_number,
        contact_email,
        delivery_address
        )
    VALUES
        (
            @new_siteID,
            @new_handsetModel,
            @new_partNumber,
            @new_faultDesc,
            @new_quantity,
            @new_contactName,
            @new_contactNumber,
            @new_contactEmail,
            @new_deliveryAddress
        );
END;

