import json
import hashlib


def generate_receipt_uuid(receipt):
    # Ensure UUID fields are empty
    receipt["header"]["uuid"] = ""
    receipt["header"]["previousUUID"] = ""
    receipt["header"]["referenceOldUUID"] = ""

    # Serialize the receipt with sorted keys and minimal spacing
    normalized_receipt = json.dumps(receipt, separators=(',', ':'), sort_keys=True)

    # Create a SHA256 hash of the normalized text
    hash_value = hashlib.sha256(normalized_receipt.encode('utf-8')).digest()

    # Convert hash to hexadecimal string
    receipt_uuid = hash_value.hex()
    return receipt_uuid


# Example usage
receipt_body = {
    "header": {
        "dateTimeIssued": "2022-06-13T00:34:00Z",
        "receiptNumber": "ZHFGG221",
        "uuid": "",
        "previousUUID": "",
        "referenceOldUUID": "",
        "currency": "EGP",
        "exchangeRate": 0,
        "orderdeliveryMode": "FC"
    },
    "documentType": {
        "receiptType": "SR",
        "typeVersion": "1.2"
    },
    "seller": {
        "rin": "704188708",
        "companyTradeName": "شركة الصوٝى",
        "branchCode": "0",
        "branchAddress": {
            "country": "EG",
            "governate": "cairo",
            "regionCity": "city center",
            "street": "16 street",
            "buildingNumber": "14BN",
            "postalCode": "74235",
            "floor": "1F",
            "room": "3R",
            "landmark": "tahrir square",
            "additionalInformation": "talaat harb street"
        },
        "deviceSerialNumber": "Test_SerialNo12",
        "activityCode": "6209"
    },
    "buyer": {
        "type": "F",
        "id": "313717919",
        "name": "taxpayer 1",
        "mobileNumber": "+201020567462",
        "paymentNumber": "987654"
    },
    "itemData": [
        {
            "internalCode": "880609",
            "description": "Samsung A02 32GB_LTE_BLACK_DS_SM-A022FZKDMEB_A022 _ A022_SM-A022FZKDMEB",
            "itemType": "GS1",
            "itemCode": "037000401629",
            "unitType": "EA",
            "quantity": 35,
            "unitPrice": 247.96000,
            "netSale": 7810.74000,
            "totalSale": 8678.60000,
            "total": 8887.04360,
            "commercialDiscountData": [
                {"amount": 867.86000, "description": "XYZ", "rate": 10}
            ],
            "itemDiscountData": [
                {"amount": 10, "description": "ABC", "rate": 5.6},
                {"amount": 10, "description": "XYZ"}
            ],
            "additionalCommercialDiscount": {"amount": 9456.1404, "description": "ABC", "rate": 10.0},
            "additionalItemDiscount": {"amount": 9456.1404, "description": "XYZ", "rate": 10.0},
            "valueDifference": 20,
            "taxableItems": [
                {"taxType": "T1", "amount": 1096.30360, "subType": "V009", "rate": 14}
            ]
        }
    ],
    "totalSales": 8678.60000,
    "totalCommercialDiscount": 867.86000,
    "totalItemsDiscount": 20,
    "extraReceiptDiscountData": [
        {"amount": 0, "description": "ABC", "rate": 10.12}
    ],
    "netAmount": 7810.74000,
    "feesAmount": 0,
    "totalAmount": 8887.04360,
    "taxTotals": [
        {"taxType": "T1", "amount": 1096.30360}
    ],
    "paymentMethod": "C",
    "adjustment": 0
}

# Wrap in a "receipts" array if needed
receipt_uuid = generate_receipt_uuid(receipt_body)
print("Generated Receipt UUID:", receipt_uuid)
