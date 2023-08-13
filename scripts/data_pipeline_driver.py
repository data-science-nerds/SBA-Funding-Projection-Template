from create_dataset import main_data_flow


def main(raw_data_file):
    data = main_data_flow(raw_data_file=raw_data_file)
    return data


if __name__ == "__main__":
    raw_data_file = "data/raw/7-09-PALS-Start-up-Financial-Projections-Custom-Template.xlsx"
    main(raw_data_file=raw_data_file)