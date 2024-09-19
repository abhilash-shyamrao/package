import { render, screen, fireEvent } from '@testing-library/react';
import DatasetRules from './DatasetRules';
import { AggregatedData } from '../../models/AggregatedData';
import { vi } from 'vitest';

describe('DatasetRules Component', () => {
    const mockData: AggregatedData = {
        dataset: {
            datasetRuleset: ['Rule 1', 'Rule 2', 'Rule 3'],
        },
    };

    it('renders table rows with dataset rules', () => {
        render(<DatasetRules data={mockData} />);

        // Check if the rules are rendered
        expect(screen.getByText('Rule 1')).toBeInTheDocument();
        expect(screen.getByText('Rule 2')).toBeInTheDocument();
        expect(screen.getByText('Rule 3')).toBeInTheDocument();
    });

    it('allows selecting and deselecting rows', () => {
        render(<DatasetRules data={mockData} />);

        const firstCheckbox = screen.getAllByRole('checkbox')[1]; // First rule checkbox
        const secondCheckbox = screen.getAllByRole('checkbox')[2]; // Second rule checkbox

        // Initially, no checkbox should be checked
        expect(firstCheckbox).not.toBeChecked();
        expect(secondCheckbox).not.toBeChecked();

        // Simulate clicking on the first checkbox
        fireEvent.click(firstCheckbox);
        expect(firstCheckbox).toBeChecked();

        // Simulate clicking on the second checkbox
        fireEvent.click(secondCheckbox);
        expect(secondCheckbox).toBeChecked();

        // Deselect the first checkbox
        fireEvent.click(firstCheckbox);
        expect(firstCheckbox).not.toBeChecked();
    });

    it('applies the correct CSS class for selected rows', () => {
        render(<DatasetRules data={mockData} />);

        const firstRow = screen.getAllByRole('row')[1]; // First rule row
        const firstCheckbox = screen.getAllByRole('checkbox')[1]; // First rule checkbox

        // Initially, the row should not have the "dr-checked" class
        expect(firstRow).not.toHaveClass('dr-checked');

        // Click the checkbox to select the row
        fireEvent.click(firstCheckbox);

        // Now the row should have the "dr-checked" class
        expect(firstRow).toHaveClass('dr-checked');
    });
});
