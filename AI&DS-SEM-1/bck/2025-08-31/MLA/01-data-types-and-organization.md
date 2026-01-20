# Data Types and Organization - 31 Aug 2025

## Data Organization in Machine Learning

### Structured Data

Structured data is information that is organized and formatted in a predictable way, making it easily searchable and processable by computers. It follows a defined data model or schema with clear relationships between data elements.

**Key characteristics:**
- Organized in rows and columns (like databases or spreadsheets)
- Has a predefined format and schema
- Easy to store, query, and analyze
- Machine-readable and searchable

**Examples:**
- Relational databases (SQL tables)
- CSV files
- XML documents
- JSON objects
- Spreadsheets

**Advantages:**
- Fast query processing
- Easy data integration
- Efficient storage
- Simple analysis and reporting
- Data consistency and integrity

### Unstructured Data

Unstructured data is information that doesn't follow a predefined data model or organizational structure, making it more challenging to process and analyze using traditional database tools.

**Key characteristics:**
- No predefined format or schema
- Difficult to organize in rows and columns
- Requires specialized tools for analysis
- Human-readable but not easily machine-processable
- Large volume and variety

**Examples:**
- Text documents (emails, reports, articles)
- Images and videos
- Audio files
- Social media posts
- Web pages
- PDFs
- Log files

**Advantages:**
- Captures rich, detailed information
- Natural format for human communication
- Flexible storage requirements
- Contains valuable insights when properly analyzed

**Challenges:**
- Requires advanced analytics tools
- Time-consuming to process
- Difficult to search and query
- Storage can be inefficient
- Data quality issues

### Classification of Data

In machine learning, data classification refers to the process of organizing and categorizing data based on specific criteria or characteristics. This classification helps determine the appropriate ML algorithms and approaches to use.

#### Based on Data Structure

**Structured Data:**
- Organized in predefined formats (tables, databases)
- Easy to process with traditional ML algorithms
- Examples: numerical datasets, categorical data in CSV files

**Unstructured Data:**
- No predefined structure or format
- Requires preprocessing and feature extraction
- Examples: text, images, audio, video files

**Semi-structured Data:**
- Partially organized with some structural elements
- Contains tags or markers for organization
- Examples: JSON, XML, HTML files

#### Based on Learning Type

**Labeled Data:**
- Contains input-output pairs
- Used for supervised learning
- Ground truth is available for training

**Unlabeled Data:**
- Contains only input data without target values
- Used for unsupervised learning
- No ground truth available

**Partially Labeled Data:**
- Mix of labeled and unlabeled instances
- Used for semi-supervised learning
- Limited labeled examples available

#### Based on Data Types

**Numerical Data:**
- Continuous or discrete numerical values
- Can be directly used in mathematical computations
- Examples: age, salary, temperature

**Categorical Data:**
- Discrete categories or classes
- Requires encoding for ML algorithms
- Examples: gender, color, product type

**Ordinal Data:**
- Categorical data with inherent order
- Maintains ranking information
- Examples: ratings (1-5 stars), education levels

**Text Data:**
- Natural language content
- Requires text preprocessing and vectorization
- Examples: documents, reviews, social media posts

**Time Series Data:**
- Data points indexed by time
- Temporal dependencies are important
- Examples: stock prices, sensor readings, weather data

#### Based on Problem Type

#### Binary Classification
Binary classification is a type of supervised machine learning task where the goal is to classify data into one of two distinct categories or classes.

**Key characteristics:**
- Only two possible output classes
- Decision boundary separates the two classes
- Output is typically 0/1, True/False, or Yes/No
- Uses algorithms like logistic regression, SVM, decision trees

**Examples:**
- Email spam detection (spam or not spam)
- Medical diagnosis (disease or no disease)
- Fraud detection (fraudulent or legitimate)
- Sentiment analysis (positive or negative)

#### Multiclass Classification
Multiclass classification is a supervised learning task where the goal is to classify data into one of three or more distinct categories.

**Key characteristics:**
- More than two possible output classes
- Each instance belongs to exactly one class
- More complex decision boundaries
- Uses algorithms like random forest, neural networks, naive Bayes

**Examples:**
- Image recognition (cat, dog, bird, etc.)
- Text categorization (sports, politics, entertainment)
- Product classification (electronics, clothing, books)
- Handwritten digit recognition (0-9)
