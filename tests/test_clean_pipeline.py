from src.clean_pipeline import clean_sales

def test_clean_sales_normalizes_and_deduplicates(tmp_path):
    source = tmp_path / 'raw.csv'
    output = tmp_path / 'clean.csv'
    source.write_text('city,sales,date\ncairo,10,2025/01/01\ncairo,,2025/01/01\n')
    result = clean_sales(source, output)
    assert len(result) == 1
    assert result.iloc[0]['city'] == 'Cairo'
    assert result.iloc[0]['date'] == '2025-01-01'
    assert output.exists()

def test_clean_sales_rejects_missing_columns(tmp_path):
    source = tmp_path / 'raw.csv'
    source.write_text('city,sales\ncairo,10\n')
    try:
        clean_sales(source, tmp_path / 'out.csv')
    except ValueError as error:
        assert 'Missing required columns' in str(error)
    else:
        raise AssertionError('Expected missing-column validation error')
