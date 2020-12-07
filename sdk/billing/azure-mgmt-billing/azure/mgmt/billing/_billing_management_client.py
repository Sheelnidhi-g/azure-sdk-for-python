# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import BillingManagementClientConfiguration
from .operations import BillingAccountsOperations
from .operations import AddressOperations
from .operations import AvailableBalancesOperations
from .operations import InstructionsOperations
from .operations import BillingProfilesOperations
from .operations import CustomersOperations
from .operations import InvoiceSectionsOperations
from .operations import BillingPermissionsOperations
from .operations import BillingSubscriptionsOperations
from .operations import ProductsOperations
from .operations import InvoicesOperations
from .operations import TransactionsOperations
from .operations import PoliciesOperations
from .operations import BillingPropertyOperations
from .operations import Operations
from .operations import BillingRoleDefinitionsOperations
from .operations import BillingRoleAssignmentsOperations
from .operations import AgreementsOperations
from .operations import EnrollmentAccountsOperations
from .operations import BillingPeriodsOperations
from . import models


class BillingManagementClient(object):
    """Billing client provides access to billing resources for Azure subscriptions.

    :ivar billing_accounts: BillingAccountsOperations operations
    :vartype billing_accounts: azure.mgmt.billing.operations.BillingAccountsOperations
    :ivar address: AddressOperations operations
    :vartype address: azure.mgmt.billing.operations.AddressOperations
    :ivar available_balances: AvailableBalancesOperations operations
    :vartype available_balances: azure.mgmt.billing.operations.AvailableBalancesOperations
    :ivar instructions: InstructionsOperations operations
    :vartype instructions: azure.mgmt.billing.operations.InstructionsOperations
    :ivar billing_profiles: BillingProfilesOperations operations
    :vartype billing_profiles: azure.mgmt.billing.operations.BillingProfilesOperations
    :ivar customers: CustomersOperations operations
    :vartype customers: azure.mgmt.billing.operations.CustomersOperations
    :ivar invoice_sections: InvoiceSectionsOperations operations
    :vartype invoice_sections: azure.mgmt.billing.operations.InvoiceSectionsOperations
    :ivar billing_permissions: BillingPermissionsOperations operations
    :vartype billing_permissions: azure.mgmt.billing.operations.BillingPermissionsOperations
    :ivar billing_subscriptions: BillingSubscriptionsOperations operations
    :vartype billing_subscriptions: azure.mgmt.billing.operations.BillingSubscriptionsOperations
    :ivar products: ProductsOperations operations
    :vartype products: azure.mgmt.billing.operations.ProductsOperations
    :ivar invoices: InvoicesOperations operations
    :vartype invoices: azure.mgmt.billing.operations.InvoicesOperations
    :ivar transactions: TransactionsOperations operations
    :vartype transactions: azure.mgmt.billing.operations.TransactionsOperations
    :ivar policies: PoliciesOperations operations
    :vartype policies: azure.mgmt.billing.operations.PoliciesOperations
    :ivar billing_property: BillingPropertyOperations operations
    :vartype billing_property: azure.mgmt.billing.operations.BillingPropertyOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.billing.operations.Operations
    :ivar billing_role_definitions: BillingRoleDefinitionsOperations operations
    :vartype billing_role_definitions: azure.mgmt.billing.operations.BillingRoleDefinitionsOperations
    :ivar billing_role_assignments: BillingRoleAssignmentsOperations operations
    :vartype billing_role_assignments: azure.mgmt.billing.operations.BillingRoleAssignmentsOperations
    :ivar agreements: AgreementsOperations operations
    :vartype agreements: azure.mgmt.billing.operations.AgreementsOperations
    :ivar enrollment_accounts: EnrollmentAccountsOperations operations
    :vartype enrollment_accounts: azure.mgmt.billing.operations.EnrollmentAccountsOperations
    :ivar billing_periods: BillingPeriodsOperations operations
    :vartype billing_periods: azure.mgmt.billing.operations.BillingPeriodsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID that uniquely identifies an Azure subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = BillingManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.billing_accounts = BillingAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.address = AddressOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_balances = AvailableBalancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.instructions = InstructionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_profiles = BillingProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.customers = CustomersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invoice_sections = InvoiceSectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_permissions = BillingPermissionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_subscriptions = BillingSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.products = ProductsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invoices = InvoicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.transactions = TransactionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_property = BillingPropertyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_role_definitions = BillingRoleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_role_assignments = BillingRoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.agreements = AgreementsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.enrollment_accounts = EnrollmentAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_periods = BillingPeriodsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> BillingManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
