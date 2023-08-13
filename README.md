# SBA-Funding-Projection-Template
SBA financial funding application including itemized projection of earnings.Use case showcased is converting a house into a pet-friendly residential assisted living facility for seniors (PALS). Ideal for entrepreneurs seeking guidance on financial documentation for SBA loans.

# To run locally with fully automated script
```
python3 scripts/data_pipeline_driver.py
```

# chatGPT prompt:
https://chat.openai.com/c/cb43e8fb-a457-4d6e-8f8e-0267e9e3464e


Pretend you are a top performing mid-level python developer.  Can you please help me write up a sample demo full codebase that showcases uses with langchain, pinecone, fast api, pydantic, textsplitter, with numeric and text data processing, including sample data. this should include a simple but appealing front end like a simple dashboard

# chatGPT suggested steps
# System Setup:
Required Python libraries.
Sample data (numeric and text).
# Backend:
Use FastAPI to create an API.
Utilize Pydantic for data validation.
Integrate TextSplitter for text processing.
(Note: I don't have direct access to specific langchain and pinecone libraries, as they are beyond my training cut-off. However, I can provide pseudo-integrations based on typical use cases for such tools).
# Frontend:
A simple dashboard using HTML/CSS/JS to interact with our FastAPI backend.

# the scope of the front end
1. Display the Data: Load the data from the provided Excel file and display it in a tabular form.
2. Identify Missing Data: Identify cells in the Excel file that have missing data and highlight them.
3. Visualization: Provide a basic visualization (like a bar chart or line chart) of numeric columns to make it human-friendly.
4. Summary: Automatically generate a text summary highlighting important information from the data.

# File Structure
SBA-Funding-Projection-Template/
│
├── app/                                  # Main application directory
│   ├── api/                              # API related modules
│   │   ├── routes/                       # Endpoints split by domain logic
│   │   │   ├── users.py
│   │   │   └── items.py
│   │   └── main.py                       # FastAPI main application instance
│   │
│   ├── models/                           # Pydantic models, data validation
│   │   ├── request_models.py             # Pydantic models for request validation
│   │   └── response_models.py            # Pydantic models for response formatting
│   │
│   ├── services/                         # Business logic, data processing, pinecone calls
│   │   ├── data_service.py
│   │   └── pinecone_service.py
│   │
│   └── db/                               # Database models, CRUD operations
│       ├── session.py                    # Database session, connection
│       └── models.py                     # ORM models (if you plan to use a database)
│
├── data/
│   ├── processed/
│   └── raw/
│       └── 7-09-PALS-Start-up-Financial-Projections-Custom-Template.xlsx
│
├── scripts/                              # Data processing scripts, ETL
│   ├── create_dataset.py
│   └── data_pipeline_driver.py
│
├── static/                               # Static files like CSS, JS
│
├── templates/                            # HTML templates for any frontend
│   └── index.html
│
├── tests/                                # Test modules
│
├── config/                               # Configuration files, .env files
│
│
├── README.md
└── requirements.txt

