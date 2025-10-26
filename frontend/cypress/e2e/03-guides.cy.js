// Build guides tests - the main one
describe('Build Guides Tests', () => {

    it('complete guide creation flow', () => {
        // Go to guides page
        cy.visit('/guides');
        cy.wait(2000);

        const username = 'testuser123';
        const title = 'My Test Build';
        const description = 'This is my test build guide description.';

        // Fill everything correctly
        cy.get('input[name="username"]').clear().type(username);

        // Pick a character from dropdown
        cy.get('select[name="character_name"]').select(1);

        // Add title
        cy.get('input[name="title"]').clear().type(title);

        // Add description
        cy.get('textarea[name="description"]').clear().type(description);

        // Submit the form
        cy.get('button[type="submit"]').click();

        // Wait for submission
        cy.wait(2000);

        // Reload page to see if guide shows up
        cy.reload();
        cy.wait(2000);

        // Should see guides on the page
        cy.get('.flex.flex-col.gap-6').should('exist');
    });

    it('shows validation requirements', () => {
        cy.visit('/guides');
        cy.wait(1000);

        // Check that form has required fields
        cy.get('input[name="username"]').should('have.attr', 'required');
        cy.get('select[name="character_name"]').should('have.attr', 'required');
        cy.get('input[name="title"]').should('have.attr', 'required');
        cy.get('textarea[name="description"]').should('have.attr', 'required');

        // Check minimum length requirements exist
        cy.get('input[name="username"]').should('have.attr', 'minlength', '4');
        cy.get('input[name="title"]').should('have.attr', 'minlength', '4');
        cy.get('textarea[name="description"]').should('have.attr', 'minlength', '10');
    });

    it('pagination works on guides page', () => {
        cy.visit('/guides');
        cy.wait(2000);

        // Should see guides section
        cy.get('.flex.flex-col.gap-6').should('exist');

        // Should see page number
        cy.get('.text-lg.font-bold').should('be.visible');

        // Should see pagination buttons
        cy.get('button.px-6').should('have.length.at.least', 2);
    });

    it('displays guide content', () => {
        cy.visit('/guides');
        cy.wait(2000);

        // Should see guide content on the page
        cy.get('img').should('have.length.at.least', 1);
        cy.get('.text-xl').should('be.visible');
        cy.get('.text-gray-700').should('be.visible');
    });

    it('fails if backend is not running', () => {
        // If backend is down, this test will fail
        cy.visit('/guides');

        // Should load page within 10 seconds
        cy.get('form', { timeout: 10000 }).should('exist');
    });
});